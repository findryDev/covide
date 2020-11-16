import requests
import json

urlConfirm = 'https://covid2019-api.herokuapp.com/timeseries/confirmed'
urlDeaths = 'https://covid2019-api.herokuapp.com/timeseries/deaths'
urlRecovery = 'https://covid2019-api.herokuapp.com/timeseries/recovered'


def requestPlotsData():
    # create world dictionary?
    #
    r = requests.get(urlConfirm)
    j = json.loads(r.text)
    listCountryConfirm = []
    dictWorldConfirm = {'country': 'World'}
    for e in j['confirmed']:
        del e["Lat"]
        del e["Long"]
        countryRegion = e['Country/Region'] + (
            ' - ' + (e['Province/State'])if e['Province/State'] != '' else '')
        dictTemp = {'country': countryRegion}
        del e["Country/Region"]
        del e["Province/State"]
        dictTemp.update(e)
        # worldDict
        # check
        for key in dictTemp:
            if key in dictWorldConfirm.keys() and key != 'country':
                dictWorldConfirm.update({key: dictTemp[key]
                                         + dictWorldConfirm[key]})
            elif key == 'country':
                pass
            else:
                dictWorldConfirm.update({key: dictTemp[key]})
        listCountryConfirm.append(dictTemp)
    listCountryConfirm.append(dictWorldConfirm)
    # listcountryConfirm = [{country: '', 'date' : n-case}, {...}]

    r = requests.get(urlDeaths)
    j = json.loads(r.text)
    listCountryDeaths = []
    dictWorldDeaths = {'country': 'World'}
    for e in j['deaths']:
        del e["Lat"]
        del e["Long"]
        countryRegion = e["Country/Region"] + (
            " - " + (e["Province/State"])if e["Province/State"] != '' else '')
        dictTemp = {'country': countryRegion}
        del e["Country/Region"]
        del e["Province/State"]
        dictTemp.update(e)
        # worldDict

        for key in dictTemp:
            if key in dictWorldDeaths.keys() and key != 'country':
                dictWorldDeaths.update({key: dictTemp[key]
                                        + dictWorldDeaths[key]})
            elif key == 'country':
                pass
            else:
                dictWorldDeaths.update({key: dictTemp[key]})
        listCountryDeaths.append(dictTemp)
    listCountryDeaths.append(dictWorldDeaths)

    r = requests.get(urlRecovery)
    j = json.loads(r.text)
    listCountryRecovered = []
    dictWorldRecovered = {'country': 'World'}
    for e in j['recovered']:
        del e["Lat"]
        del e["Long"]
        countryRegion = e["Country/Region"] + (
            " - " + (e["Province/State"])if e["Province/State"] != '' else '')
        dictTemp = {'country': countryRegion}
        del e["Country/Region"]
        del e["Province/State"]
        dictTemp.update(e)
        # worldDict
        for key in dictTemp:
            if key in dictWorldRecovered.keys() and key != 'country':
                dictWorldRecovered.update({key: dictTemp[key]
                                          + dictWorldRecovered[key]})
            elif key == 'country':
                pass
            else:
                dictWorldRecovered.update({key: dictTemp[key]})
        listCountryRecovered.append(dictTemp)
    listCountryRecovered.append(dictWorldRecovered)
    #   summaryDict{country:{confirm:{date:case},
    #                       inDayConfirm:{date: inOneDayCases}
    #                       maxInDayConfirm{date:maxConfirmCases}
    #                       deaths:{date:case},
    #                       inDayDeaths:{date: inOneDayCases}
    #                       maxInDayDeaths{date:maxDeathsCases}
    #                       recovery:{date:case},
    #                       inDayRecovered:{date: inOneDayCases}
    #                       maxInDayRecovered{date:maxRecoveredCases}}}}
    # create world summary dict ?
    summaryDict = {}
    valueList = []
    keyList = []

    for e in listCountryConfirm:
        country = e['country']
        del e['country']
        summaryDict.update({country: {}})
        summaryDict[country].update({'confirm': {}})
        summaryDict[country].update({'inDayConfirm': {}})
        summaryDict[country].update({'maxInDayConfirm': {}})
        summaryDict[country]['confirm'].update(e)
        valueList = list(summaryDict[country]['confirm'].values())
        keyList = list(summaryDict[country]['confirm'].keys())
        for i in range(len(keyList)-1):
            summaryDict[country]['inDayConfirm'].update(
                {keyList[i+1]: valueList[i+1] - valueList[i]if
                 valueList[i+1] - valueList[i] > 0
                 else 0})
        dayCaseDict = summaryDict[country]['inDayConfirm']
        maxKey = max(dayCaseDict, key=dayCaseDict.get)
        maxValue = dayCaseDict[maxKey]
        summaryDict[country]['maxInDayConfirm'].update({maxKey: maxValue})

    for e in listCountryDeaths:
        country = e['country']
        del e['country']
        if country not in summaryDict.keys():
            summaryDict.update({country: {'deaths': {}}})
        summaryDict[country].update({'deaths': {}})
        summaryDict[country].update({'inDayDeaths': {}})
        summaryDict[country].update({'maxInDayDeaths': {}})
        summaryDict[country]['deaths'].update(e)
        valueList = list(summaryDict[country]['deaths'].values())
        keyList = list(summaryDict[country]['deaths'].keys())
        for i in range(len(keyList)-1):
            summaryDict[country]['inDayDeaths'].update(
                {keyList[i+1]: valueList[i+1] - valueList[i]if
                 valueList[i+1] - valueList[i] > 0
                 else 0})
        dayCaseDict = summaryDict[country]['inDayDeaths']
        maxKey = max(dayCaseDict, key=dayCaseDict.get)
        maxValue = dayCaseDict[maxKey]
        summaryDict[country]['maxInDayDeaths'].update({maxKey: maxValue})

    for e in listCountryRecovered:
        country = e['country']
        del e['country']
        if country not in summaryDict.keys():
            summaryDict.update({country: {'recovered': {}}})
        summaryDict[country].update({'recovered': {}})
        summaryDict[country].update({'inDayRecovered': {}})
        summaryDict[country].update({'maxInDayRecovered': {}})
        summaryDict[country]['recovered'].update(e)
        valueList = list(summaryDict[country]['recovered'].values())
        keyList = list(summaryDict[country]['recovered'].keys())
        for i in range(len(keyList)-1):
            summaryDict[country]['inDayRecovered'].update(
                {keyList[i+1]: valueList[i+1] - valueList[i] if
                 valueList[i+1] - valueList[i] > 0
                 else 0})
        dayCaseDict = summaryDict[country]['inDayRecovered']
        maxKey = max(dayCaseDict, key=dayCaseDict.get)
        maxValue = dayCaseDict[maxKey]
        summaryDict[country]['maxInDayRecovered'].update({maxKey: maxValue})

    with open('summary.json', 'w') as f:
        json.dump(summaryDict, f)
    return summaryDict
