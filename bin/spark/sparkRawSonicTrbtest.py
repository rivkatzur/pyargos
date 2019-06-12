import sys
import json
import pandas
from datetime import datetime
from pyspark.sql import Row, SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pymeteo.analytics.turbulencecalculator import TurbulenceCalculatorSpark
import paho.mqtt.client as mqtt
from pyargos.thingsboard.tbHome import tbHome
import argparse

credentialMap = {}

connectionMap = {}
window_in_seconds = None

with open('/home/yehudaa/Projects/2019/TestExp/experimentConfiguration.json') as credentialOpen:
    credentialMap = json.load(credentialOpen)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed")


def getClient(deviceName):
    if deviceName in connectionMap:
        client = connectionMap[deviceName]
    else:
        tbh = tbHome(credentialMap["connection"])
        accessToken = tbh.deviceHome.createProxy(deviceName).getCredentials()
        client = mqtt.Client("Me")
        client.on_connect = on_connect

        client.username_pw_set(str(accessToken), password=None)
        try:

            client.connect(host=credentialMap["connection"]['server']['ip'],port=1883)
        except Exception as e:
            print(e)
            print('connection failed')
            raise e

        print('connection succeed')
        connectionMap[deviceName] = client
        client.loop_start()
    return client


def getSparkSessionInstance(sparkConf):
    try:
        if ("sparkSessionSingletonInstance" not in globals()):
            globals()["sparkSessionSingletonInstance"] = SparkSession \
                .builder \
                .config(conf=sparkConf) \
                .getOrCreate()
        return globals()["sparkSessionSingletonInstance"]
    except:
        print('failed1')

def process(time, rdd):
    print("========= %s =========" % str(time))
    try:
        # Get the singleton instance of SparkSession
        spark = getSparkSessionInstance(rdd.context.getConf())

        # Convert RDD[String] to RDD[Row] to DataFrame
        rowRdd = rdd.map(lambda data: Row(Device=str(data['deviceName']),
                                          Time=datetime.fromtimestamp(float(data['ts']) / 1000.0),
                                          u=float(data['u']),
                                          v=float(data['v']),
                                          w=float(data['w']),
                                          T=float(data['T'])
                                          )
                         )
        wordsDataFrame = spark.createDataFrame(rowRdd)
        # print(wordsDataFrame.toPandas())
        for x in wordsDataFrame.toPandas().groupby("Device"):
            data = x[1].set_index('Time')[['T', 'u', 'v', 'w']]

            # print('----------%s----------'%(deviceName))
            resampledData = data.resample('%ds' % (window_in_seconds)).count()
            print(resampledData[['T']].rename(columns={'T':'count'}))
            numOfTimeIntervals = len(resampledData)
            if (numOfTimeIntervals > 2):
                deviceName = "%s_%ds" % (x[0], window_in_seconds)
                # deviceName = "Device_10s"
                startTime = pandas.datetime.time(resampledData.index[numOfTimeIntervals-2])
                endTime = pandas.datetime.time(resampledData.index[numOfTimeIntervals-2] + pandas.Timedelta('%ds' % (window_in_seconds)))
                data = data.between_time(startTime, endTime)
                trbCalc = TurbulenceCalculatorSpark(data, identifier={'samplingWindow': "%ds" % (window_in_seconds)}, metadata=None)
                calculatedParams = trbCalc.uu().vv().ww().compute()

                timeCalc = calculatedParams.index[0]
                values = calculatedParams.T.to_dict()[timeCalc]
                values['count'] = resampledData.iloc[numOfTimeIntervals-2]['T']
                values['frequency'] = values['count']/window_in_seconds

                # print(timeCalc,values)
                client = getClient(deviceName)
                client.publish('v1/devices/me/telemetry', str({"ts": int(1000 * (datetime.timestamp(timeCalc))),
                                                               "values": values
                                                               }
                                                              )
                   )
    # wordsDataFrame.show()
    except Exception as e:
        print(e)

if __name__ == "__main__":

    # argparse
    # read the config file with the connection paramters.
    # use padnas timedelta to set windows_in_seconds with total_seconds().

    globals()

    parser = argparse.ArgumentParser()
    parser.add_argument("--window", dest="window", help="The spark window time", required=True, type=str)
    parser.add_argument("--broker", dest="broker", help="The broker", required=True, type=str)
    parser.add_argument("--topic", dest="topic", help="The topic", required=True, type=str)
    args = parser.parse_args()

    window_in_seconds = pandas.Timedelta(args.window).seconds
    sc = SparkContext(appName="PythonStreamingDirectKafkaWordCount")
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, window_in_seconds)
    brokers = args.broker
    topic = args.topic
    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
    lines = kvs.map(lambda x: x[1])
    linesAsJson = lines.map(lambda x: json.loads(x)).window(3 * window_in_seconds, window_in_seconds)
    try:
        linesAsJson.foreachRDD(process)
    except('Stop Iteration'):
        pass

    ssc.start()
    ssc.awaitTermination()
    for _, client in connectionMap:
        client.loop_stop()
        client.disconnect()