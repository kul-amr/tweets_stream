import json
import os
import psycopg2
from dateutil import parser
from settings import POSTGRESDB_PWD
from kafka import KafkaConsumer


POSTGRESDB_PWD = os.environ.get('POSTGRESDB_PWD')

consumer = KafkaConsumer("job_tweets",
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='latest',
                         enable_auto_commit=True,
                         group_id=None,
                         key_deserializer=lambda k: json.loads(k.decode('utf-8')),
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')))


def store_tweets():
    print("in store_tweets to db")
    conn = psycopg2.connect(
        database="software_jobs", user="postgres", password=POSTGRESDB_PWD,
        host='localhost')

    cursor = conn.cursor()

    print("conn cursor ready")

    for msg in consumer:
        print(msg)
        tweet_id = msg.key['tweet_id']
        tweet_text = msg.value['tweet_text']
        tweet_job_url = msg.value['job_url']
        created_at = parser.parse(msg.value['created_at'])

        # cursor.execute('''INSERT INTO software_jobs(tweet_id,tweet_text,job_url,created_at)
        #                     VALUES (%s, %s, %s, %s)''',
        #                (int(tweet_id), tweet_text, tweet_job_url, created_at))

        sql = '''with job_key as (
                        INSERT INTO software_jobs(tweet_id,tweet_text,job_url,created_at)
                        VALUES (%s, %s, %s, %s)
                        returning id
                        )
                        INSERT INTO notifications(job_id, is_viewed)
                        SELECT id, False FROM job_key
                        '''
        cursor.execute(sql, (int(tweet_id), tweet_text, tweet_job_url, created_at))

        conn.commit()

    # print("out of for loop")
    conn.close()


store_tweets()
