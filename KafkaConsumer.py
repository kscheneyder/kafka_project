from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
from s3fs import S3FileSystem
import json

#creating the funcion to consum the data
consumer = KafkaConsumer(
    'kafka_project',
    bootstrap_servers = ['00.000.00.00:9092'], #ADD YOUR IP HERE
    value_deserializer = lambda x: loads(x.decode('UTF-8')))

#Use the key and the secret downloaded from AWS
s3 = S3FileSystem(key='', secret='')

#storing data on real time do S3 bucket
for count, i in enumerate(consumer):
    with s3.open("s3://kafka-covid-data-scheneyder/covid_death_us_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)
