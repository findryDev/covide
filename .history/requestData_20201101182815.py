import requests
import json
import pandas as pd

urlConfirm = 'https://covid2019-api.herokuapp.com/timeseries/confirmed'
urlDeaths = 'https://covid2019-api.herokuapp.com/timeseries/deaths'
urlRcovery = 'https://covid2019-api.herokuapp.com/timeseries/recovered'


r = requests.get(urlConfirm)
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


#listcountryConfirm = [{country: '', 'date' : n-case}, {...}]

r = requests.get(urlDeaths)
j = json.loads(r.text)
listCountryConfirm = []
for e in j['']:
    del e["Lat"]
    del e["Long"]
    countryRegion = e["Country/Region"] + (" - " + (e["Province/State"])if e["Province/State"] != '' else '')
    dictTemp = {'country': countryRegion}
    del e["Country/Region"]
    del e["Province/State"]
    dictTemp.update(e)
    listCountryConfirm.append(dictTemp)

r = requests.get(urlRcovery)
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