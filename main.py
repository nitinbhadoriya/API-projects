import requests
import requests_cache
import json
import time
from IPython.core.display import clear_output
requests_cache.install_cache()

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def last_fm_requests(payload):
    headers = {
        'user-agent': USER_AGENT
    }
    url='https://ws.audioscrobbler.com/2.0/'
    r = requests.get(url, headers = headers, params = payload)
    return r

API_KEY = 'c388e2286deda45d940563f3fae64a21'
USER_AGENT = 'MusicAPI'

responses=[]
page=1
total_pages=99999

while page<=total_pages:
    payload = {
        'api_key': API_KEY,
        'method': 'chart.gettopartists',
        'limit': 500,
        'page' :page,
        'format': 'json'
    }
    print("Requesting page{}/{}".format(page,total_pages))
    clear_output(wait=True)
    response= last_fm_requests(payload)

    if response.status_code!=200:
        print(response.text)
        break
    page =int(response.json()['artists']['@attr']['page'])
    total_pages=int(response.json()['artists']['@attr']['totalPages'])
    responses.append(response)

    if not getattr(response,'from_cache', False):
        time.sleep(0.25)
    page+=1

