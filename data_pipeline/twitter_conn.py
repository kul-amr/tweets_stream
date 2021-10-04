import os
import settings

bearer_token = os.environ.get('TWITTER_API_BEARER_TOKEN')


def bearer_oauth(r):

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r
