import requests
import re
import json
from config import *
from twitter_conn import *
from kafka import KafkaProducer

# logging.basicConfig(level=logging.DEBUG)
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         key_serializer=lambda k: json.dumps(k).encode('utf-8'),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))


def process_tweets_stream():

    counter = 0

    with requests.Session().get(TWITTER_STREAM_URL, auth=bearer_oauth, stream=True) as response:
        print(response)
        if response.status_code != 200:
            raise Exception(
                "Error in getting tweets stream (HTTP {}): {}".format(response.status_code, response.text)
            )
        else:
            for response_line in response.iter_lines():
                print(response_line)
                if counter < 50:
                    if response_line:
                        json_response = json.loads(response_line)
                        # print(json.dumps(json_response, indent=4, sort_keys=True))
                        tweet_text = json_response['data']['text']
                        tweet_id = json_response['data']['id']
                        created_at = json_response['data']['created_at']
                        tweet_urls = find_tweet_url(tweet_text)
                        for t_url in tweet_urls:
                            key = {"tweet_id": tweet_id}
                            val = {"tweet_text": tweet_text,
                                   "job_url": t_url,
                                   "created_at": created_at}
                            send_to_producer(key, val)
                        counter += 1
                else:
                    return


def find_tweet_url(tweet_text):
    return re.findall(r'(https?://[^\s]+)', tweet_text)


def send_to_producer(key, val):
    print("kafka producer sending msg ")
    producer.send("job_tweets", key=key, value=val)
    print("kafka producer msg sent ")


process_tweets_stream()


##hashtags - top hashtags
##top dbs
##top coding lang
##languages
##ios,android,backend,data,fullstack,frontend,devops,cloud,systems,AI,ML
##junior/senior/manager
##tweets having salary info
##contract/full-time/internship
##remote jobs sentiment analysis