import requests
import json
import pandas as pd

url = 'https://covid2019-api.herokuapp.com/timeseries/confirmed'

r = requests(url)
print(r.text)