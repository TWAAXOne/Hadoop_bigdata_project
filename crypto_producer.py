# Kafka Producer- Produces the Streaming API Data
from json import dumps
from kafka import KafkaProducer
import tweepy
import configparser
from datetime import datetime, timedelta

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

lst_search = ['Bitcoin', 'BTC', 'Bitcoin price', 'bitcoin analyse']
for i in range(4):
    bitcoin_tweets = api.search_tweets(lst_search[i], count=100, lang="en", result_type="mixed", until=yesterday.strftime("%Y-%m-%d"))

    # Kafka Producer
    for tweet in bitcoin_tweets:
        print(tweet._json)  # print the tweet
        producer.send('monApp', tweet._json)  # send the tweet to the topic monApp