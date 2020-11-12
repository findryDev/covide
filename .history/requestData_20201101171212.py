import requests
import json
import pandas as pd

url = 'https://covid2019-api.herokuapp.com/timeseries/confirmed'

r = requests.get(url)
j = json.loads(r.text)
print(j.)