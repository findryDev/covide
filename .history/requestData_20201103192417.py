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
    countryRegion = e['Country/Region'] + (' - ' + (e['Province/State'])if e['Province/State'] != '' else '')
    dictTemp = {'country': countryRegion}
    del e["Country/Region"]
    del e["Province/State"]
    dictTemp.update(e)
    listCountryConfirm.append(dictTemp)

# listcountryConfirm = [{country: '', 'date' : n-case}, {...}]

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
    listCountryDeaths.append(dictTemp)

r = requests.get(urlRecovery)
j = json.loads(r.text)
listCountryRecovered = []
for e in j['recovered']:
    del e["Lat"]
    del e["Long"]
    countryRegion = e["Country/Region"] + (" - " + (e["Province/State"])if e["Province/State"] != '' else '')
    dictTemp = {'country': countryRegion}
    del e["Country/Region"]
    del e["Province/State"]
    dictTemp.update(e)
    listCountryRecovered.append(dictTemp)

summaryDict = {}
valueList = []
keyList = []

for e in listCountryConfirm:
    country = e['country']
    del e['country']
    summaryDict.update({country: {}})
    summaryDict[country].update({'confirm': {}})
    summaryDict[country].update({'inDayConfirm': {}})
    summaryDict[country]['confirm'].update(e)
    valueList = list(summaryDict[country]['confirm'].values())
    keyList = list(summaryDict[country]['confirm'].keys())
    for i in range(len(keyList)):
        summaryDict[country]['inDayConfirm'].update({keyList[i]: valueList[i+1] - valueList[i]})

for e in listCountryDeaths:
    country = e['country']
    del e['country']
    if country not in summaryDict.keys(): summaryDict.update({country: {'deaths': {}}})
    summaryDict[country].update({'deaths': {}})
    summaryDict[country].update({'inDayDeaths': {}})
    summaryDict[country]['deaths'].update(e)
    valueList = list(summaryDict[country]['deaths'].values())
    keyList = list(summaryDict[country]['deaths'].keys())
    for i in range(len(keyList)):
        summaryDict[country]['inDayDeaths'].update({keyList[i]: valueList[i+1] - valueList[i]})

for e in listCountryRecovered:
    country = e['country']
    del e['country']
    if country not in summaryDict.keys(): summaryDict.update({country: {'recovered': {}}})
    summaryDict[country].update({'recovered': {}})
    summaryDict[country].update({'inDayRecovered': {}})
    summaryDict[country]['recovered'].update(e)
    valueList = list(summaryDict[country]['recovered'].values())
    keyList = list(summaryDict[country]['recovered'].keys())
    for i in range(len(keyList)):
        summaryDict[country]['inDayRecovered'].update({keyList[i]: valueList[i+1] - valueList[i]})
