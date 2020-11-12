import requests
import json
import pandas as pd

urlConfirm = 'https://covid2019-api.herokuapp.com/timeseries/confirmed'
urlDeaths = 'https://covid2019-api.herokuapp.com/timeseries/deaths'
urlRecovery = 'https://covid2019-api.herokuapp.com/timeseries/recovered'


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
listCountryDeaths = []
for e in j['deaths']:
    del e["Lat"]
    del e["Long"]
    countryRegion = e["Country/Region"] + (" - " + (e["Province/State"])if e["Province/State"] != '' else '')
    dictTemp = {'country': countryRegion}
    del e["Country/Region"]
    del e["Province/State"]
    dictTemp.update(e)
    listCountryConfirm.append(dictTemp)

r = requests.get(urlRecovery)
j = json.loads(r.text)
listCountryRecovery = []
for e in j['recovered']:
    del e["Lat"]
    del e["Long"]
    countryRegion = e["Country/Region"] + (" - " + (e["Province/State"])if e["Province/State"] != '' else '')
    dictTemp = {'country': countryRegion}
    del e["Country/Region"]
    del e["Province/State"]
    dictTemp.update(e)
    listCountryConfirm.append(dictTemp)

summaryDict = {}

for e in listCountryConfirm:
    country = e['country']
    del e['country']
    summaryDict = {country: {'confirm' : {}}}
    summaryDict[country]['confirm'].update(e)


    print(summaryDict['poland'])

for e in listCountryDeaths:
    print(e['country'])

for e in listCountryRecovery:
    print(e['country'])

