import requests
import json
from twitter_conn import *

tweet_id = 1442849832998158347
annotations_url = f"https://api.twitter.com/2/tweets/{tweet_id}?tweet.fields=context_annotations"


def get_tweet_annotations():

    with requests.Session().get(annotations_url, auth=bearer_oauth) as response:
        print(response)
        for response_line in response.iter_lines():
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))
            twt_id = json_response['data']['id']
            twt_text = json_response['data']['text']
            entities = []

            if 'context_annotations' in json_response['data']:
                for d in json_response['data']['context_annotations']:
                    entities.append(d['entity'])

            tweet_obj = {'id': twt_id, 'txt': twt_text, 'entities': entities}

            print(tweet_obj)


get_tweet_annotations()