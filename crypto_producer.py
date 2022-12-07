#Kafka Producer- Produces the Streaming API Data
from time import sleep
from json import dumps
import requests
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='sandbox-hdp.hortonworks.com:6667',

                         value_serializer=lambda x: dumps(x).encode('utf-8'),

                         api_version=(0, 10, 1))
res = requests.get("https://jsonplaceholder.typicode.com/users",stream=True)
djson = res.text
datajson = json.loads(djson)

#print(datajson)

for data in datajson:
    print(data)
    producer.send('crypto2', data)
