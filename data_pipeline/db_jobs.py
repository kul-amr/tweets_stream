import psycopg2
from settings import POSTGRESDB_PWD


conn = psycopg2.connect(
    database="software_jobs", user="postgres", password=POSTGRESDB_PWD,
    host='localhost')

cursor = conn.cursor()
cursor.execute('''DROP TABLE IF EXISTS software_jobs''')

sql = '''CREATE TABLE software_jobs(
        id SERIAL PRIMARY KEY,
        tweet_id VARCHAR(20),
        tweet_text VARCHAR(300),
        job_url VARCHAR(200),
        created_at timestamptz NOT NULL DEFAULT now()
        )'''

cursor.execute(sql)
conn.commit()
conn.close()
