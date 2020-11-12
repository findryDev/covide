import requestData
import json
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd


# load data from file
data = requestData.requestPlotsData()
# current country. will be loop for dict key


def create_plot(dataPlots, country):
    # size of plot
    data = dataPlots
    ratio = 2/4
    width = 30
    height = ratio * width
    widthHeight = (width, height)
    plt.figure(figsize=widthHeight)
    # assigned variable
    countryData = data[country]
    # create df from data
    if 'confirm' in data[country].keys():
        confirmData = pd.DataFrame(list(zip(countryData['confirm'].keys(),
                                        countryData['confirm'].values(),
                                        countryData['inDayConfirm'].values())),
                                        columns=['Date',
                                                 'AllCaseConfirm',
                                                 'InDayConfirm'])
        confirmData['Date'] = pd.to_datetime(confirmData['Date'])
        confirmData.sort_values('Date', inplace=True)
    else:
        confirmData = None

    if 'deaths' in data[country].keys():
        deathsData = pd.DataFrame(list(zip(countryData['deaths'].keys(),
                                    countryData['deaths'].values(),
                                    countryData['inDayDeaths'].values())),
                                    columns=['Date', 'AllCaseDeaths', 'InDayDeaths'])
        deathsData['Date'] = pd.to_datetime(deathsData['Date'])
        deathsData.sort_values('Date', inplace=True)
    else:
        deathsData = None

    if 'recovered' in data[country].keys():
        recoveredData = pd.DataFrame(list(zip(countryData['recovered'].keys(),
                                        countryData['recovered'].values(),
                                        countryData['inDayRecovered'].values())),
                                        columns=['Date', 'AllCaseRecovered', 'InDayRecovered'])
        recoveredData['Date'] = pd.to_datetime(recoveredData['Date'])
        recoveredData.sort_values('Date', inplace=True)
    else:
        recoveredData = None

    # set axisX
    if confirmData is not None:
        xAxis = confirmData['Date']
    elif deathsData is not None:
        xAxis = deathsData['Date']
    elif recoveredData is not None:
        xAxis = recoveredData['Date']
    else:
        xAxis = None
    # set axisY
    if confirmData is not None:
        # yAxisConfirmAll = confirmData['AllCaseConfirm']
        yAxisConfirmInDay = confirmData['InDayConfirm']
    else:
        # yAxisConfirmAll = None
        yAxisConfirmInDay = None

    if deathsData is not None:
        # yAxisDeathsAll = deathsData['AllCaseDeaths']
        yAxisDeathsInDay = deathsData['InDayDeaths']
    else:
        # yAxisDeathsAll = None
        yAxisDeathsInDay = None

    if recoveredData is not None:
        # yAxisRecoveredAll = recoveredData['AllCaseRecovered']
        yAxisRecoveredInDay = recoveredData['InDayRecovered']
    else:
        yAxisRecoveredAll = None
        yAxisRecoveredInDay = None

    # plots create
    # plt.plot_date(xAxis, yAxisConfirmAll, label='ConfirmAll', color='yellow', marker='.',
    #               linestyle='-')
    if confirmData is not None:
        plt.plot_date(xAxis, yAxisConfirmInDay, label='Confirm In day', color='yellow',
                    linestyle='-')
    # plot deaths
    # plt.plot_date(xAxis, yAxisDeathsAll, label='Deaths', color='black', marker='.',
    #               linestyle='--')
    if deathsData is not None:
        plt.plot_date(xAxis, yAxisDeathsInDay, label='Deaths In Day', color='black',
                    linestyle='--')
    # plot recovery
    # plt.plot_date(xAxis, yAxisRecoveredAll, label='Recovered', color='green', marker='.',
    #               linestyle='-.')
    if recoveredData is not None:
        plt.plot_date(xAxis, yAxisRecoveredInDay, label='Recovered', color='green',
                    linestyle='-.')
    #plots settings
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.xlabel('Date', fontsize=15)
    plt.ylabel('Cases', fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title(f'{country}', fontsize=20)
    plt.legend(fontsize=18)
    plt.tick_params(labelrotation=90)
    plt.grid()
    plt.tight_layout()
    plt.savefig(f'plots/{country.replace("*", "")}.png')
    print(f'create {country} plot')
    plt.cla()   # Clear axis
    plt.clf()   # Clear figure
    # plt.show()


for key in data:
    create_plot(data, key)

