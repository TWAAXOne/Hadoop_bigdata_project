# Kafka Producer- Produces the Streaming API Data
from json import dumps
from kafka import KafkaProducer
import tweepy
import configparser
from datetime import datetime, timedelta
import requests

# Kafka Producer
producer = KafkaProducer(bootstrap_servers='sandbox-hdp.hortonworks.com:6667',
                         value_serializer=lambda x: dumps(x).encode('utf-8'),
                         api_version=(0, 10, 1))

# Configs for Twitter API
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication for Twitter API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)
yesterday = datetime.today() - timedelta(days=1)  # get the date of yesterday
bitcoin_tweets = api.search_tweets("Bitcoin chart", count=100, lang="en", result_type="mixed", until=yesterday.strftime("%Y-%m-%d"))

# Kafka Producer
for tweet in bitcoin_tweets:
    print(tweet._json)  # print the tweet
    producer.send('monApp', tweet._json)  # send the tweet to the topic crypto2
# res = requests.get("https://jsonplaceholder.typicode.com/users",stream=True)
# djson = res.text
# datajson = json.loads(djson)
#
# for data in datajson:
#     print(data)
#     producer.send('monApp',data)