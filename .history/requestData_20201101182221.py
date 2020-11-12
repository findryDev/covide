import requests
import json
import pandas as pd

url = 'https://covid2019-api.herokuapp.com/timeseries/confirmed'

r = requests.get(url)
j = json.loads(r.text)
listCountryConfirm = []
for e in j['confirmed']:
    del e["Lat"]
    del e["Long"]
    countryRegion = e["Country/Region"] + (" - " + (e["Province/State"])if e["Province/State"] != '' else '')
    dictTemp = {'country': countryRegion}
    del e["Country/Region"]
    del e["Province/State"]
    dictTemp.update(e)
    listCountryConfirm.append(dictTemp)


#country