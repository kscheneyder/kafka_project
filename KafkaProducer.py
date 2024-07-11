#pip install kafka-python
import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps
import json

#creating the producer function
producer = KafkaProducer(bootstrap_servers=['00.000.00.00:9092'], #change for your ip here
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

#reading the csv file
df = pd.read_csv('us_deaths.csv')

#manipulation data as a streamming data and sending to kafka
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('kafka_project', value = dict_stock)
    sleep(1)

#clear data from kafka server
#producer.flush()
