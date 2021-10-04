import os
import dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_file = os.path.join(BASE_DIR, ".env")


if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
    TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
    TWITTER_API_KEY_SECRET = os.environ.get('TWITTER_API_KEY_SECRET')
    TWITTER_API_BEARER_TOKEN = os.environ.get('TWITTER_API_BEARER_TOKEN')
    TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
    TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    POSTGRESDB_PWD = os.environ.get('POSTGRESDB_PWD')