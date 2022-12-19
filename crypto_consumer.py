# Kafka Consumer- Consumes the produced data

from kafka import KafkaConsumer
from json import loads, dumps
from subprocess import Popen, PIPE

# Kafka Consumer
Popen(["hdfs", "dfs", "-rm", "/user/root/sortie.json"], stdout=PIPE, stderr=PIPE)  # delete the file sortie.json
put = Popen(["hadoop", "fs", "-put", "-", "/user/root/sortie.json"], stdin=PIPE, bufsize=-1)  # put the data into HDFS

consumer = KafkaConsumer(
    'monApp',  # topic name
    bootstrap_servers='sandbox-hdp.hortonworks.com:6667',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    consumer_timeout_ms=40000,
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    api_version=(0, 10, 1)
)

put.stdin.write(b'[')  # write '[' into HDFS
print(consumer)  # print the consumer
for message in consumer:
    message = message.value
    print(message)
    # Conversion en byte car attend un byte et non un str
    put.stdin.write(str.encode(dumps(message)))  # write the data into HDFS
    # Conversion en byte car attend un byte et non un str
    put.stdin.write(b",")

# Conversion en byte car attend un byte et non un str
put.stdin.write(b'{}')
put.stdin.write(b']')  # write ']' into HDFSv
# Conversion en byte car attend un byte et non un str
put.stdin.close()
put.wait()  # wait for the process to finish
