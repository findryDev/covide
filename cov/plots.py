from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd
import logging
import datetime

# create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create handlers
print_handler = logging.StreamHandler()
file_handler = logging.FileHandler('createPlots.log')
print_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)
# create formatters and add it to handlers
print_format = logging.Formatter(('%(asctime)s'
                                  ' - %(message)s'))
print_handler.setFormatter(print_format)
file_format = logging.Formatter(('%(levelname)s'
                                 ' - %(asctime)s'
                                 ' - %(message)s'
                                 ' - %(name)s'))
file_handler.setFormatter(file_format)
# add handler to the logger
logger.addHandler(print_handler)
logger.addHandler(file_handler)


def create_plot(dataPlots):
    for country in dataPlots:
        if country != 'dt':
            # size of plot
            ratio = 2/4
            width = 30
            height = ratio * width
            widthHeight = (width, height)
            plt.figure(figsize=widthHeight)
            # Setting the background color
            ax = plt.axes()
            ax.set_facecolor("grey")
            # assigned variable country data
            countryData = dataPlots[country]
            # create df from countryData
            if 'confirm' in dataPlots[country].keys():
                zipList = list(zip(countryData['confirm'].
                                   keys(),
                                   countryData['confirm'].
                                   values(),
                                   countryData['inDayConfirm'].
                                   values()))
                confirmData = pd.DataFrame(zipList,
                                           columns=['Date',
                                                    'AllCaseConfirm',
                                                    'InDayConfirm'])
                confirmData['Date'] = pd.to_datetime(confirmData['Date'])
                confirmData.sort_values('Date', inplace=True)
            else:
                confirmData = None

            if 'deaths' in dataPlots[country].keys():
                zipList = list(zip(countryData['deaths'].
                                   keys(),
                                   countryData['deaths'].
                                   values(),
                                   countryData['inDayDeaths'].
                                   values()))
                deathsData = pd.DataFrame(zipList,
                                          columns=['Date',
                                                   'AllCaseDeaths',
                                                   'InDayDeaths'])
                deathsData['Date'] = pd.to_datetime(deathsData['Date'])
                deathsData.sort_values('Date', inplace=True)
            else:
                deathsData = None

            if 'recovered' in dataPlots[country].keys():
                zipList = list(zip(countryData['recovered'].
                                   keys(),
                                   countryData['recovered'].
                                   values(),
                                   countryData['inDayRecovered'].
                                   values()))
                recoveredData = pd.DataFrame(zipList,
                                             columns=['Date',
                                                      'AllCaseRecovered',
                                                      'InDayRecovered'])
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
                # yAxisRecoveredAll = None
                yAxisRecoveredInDay = None

            # plots create
            # plt.plot_date(xAxis, yAxisConfirmAll,
            #               label='ConfirmAll',
            #               color='yellow',
            #               marker='.',
            #               linestyle='-')
            if confirmData is not None:
                plt.plot_date(xAxis, yAxisConfirmInDay,
                              label='Confirm in day',
                              color='yellow',
                              linestyle='-')
                # set text (max confirm)
                tempDataString = list(countryData['maxInDayConfirm'].keys())[0]
                currentCentry = 2000
                xCorText = datetime.date(year=int(tempDataString.split("/")[2])
                                         + currentCentry,
                                         month=int(tempDataString.split("/")
                                                   [0]),
                                         day=int(tempDataString.split("/")[1]))
                yCorText = list(countryData['maxInDayConfirm'].values())[0]
                plt.text(xCorText,
                         yCorText,
                         'max confirm cases',
                         fontsize=18,
                         color='yellow',
                         horizontalalignment='right')
            # plot deaths
            # plt.plot_date(xAxis, yAxisDeathsAll,
            #               label='Deaths',
            #               color='black',
            #               marker='.',
            #               linestyle='--')
            if deathsData is not None:
                plt.plot_date(xAxis, yAxisDeathsInDay,
                              label='Deaths in day',
                              color='black',
                              linestyle='--')
                # set text (max deaths)
                tempDataString = list(countryData['maxInDayDeaths'].keys())[0]
                currentCentry = 2000
                xCorText = datetime.date(year=int(tempDataString.split("/")[2])
                                         + currentCentry,
                                         month=int(tempDataString.split("/")
                                                   [0]),
                                         day=int(tempDataString.split("/")[1]))
                yCorText = list(countryData['maxInDayDeaths'].values())[0]
                plt.text(xCorText,
                         yCorText,
                         'max deaths cases',
                         fontsize=18,
                         color='black',
                         horizontalalignment='right')
            # plot recovery
            # plt.plot_date(xAxis, yAxisRecoveredAll,
            #               label='Recovered',
            #               color='green',
            #               marker='.',
            #               linestyle='-.')
            if recoveredData is not None:
                plt.plot_date(xAxis, yAxisRecoveredInDay,
                              label='Recovered in day',
                              color='green',
                              linestyle='-.')
                # set text (max recovered)
                tempDataString = list(countryData['maxInDayRecovered'].
                                      keys())[0]
                currentCentry = 2000
                xCorText = datetime.date(year=int(tempDataString.split("/")[2])
                                         + currentCentry,
                                         month=int(tempDataString.split("/")
                                                   [0]),
                                         day=int(tempDataString.split("/")[1]))
                yCorText = list(countryData['maxInDayRecovered'].values())[0]
                plt.text(xCorText,
                         yCorText,
                         'max rovered cases',
                         fontsize=18,
                         color='green',
                         horizontalalignment='right')
            # plots settings
            date_format = mpl_dates.DateFormatter('%d-%m-%Y')
            plt.gca().xaxis.set_major_formatter(date_format)
            plt.xlabel('Date', fontsize=15)
            plt.ylabel('Cases', fontsize=15)
            plt.xticks(fontsize=15, rotation=90)
            plt.yticks(fontsize=15, rotation=0)
            plt.title(f'{country}', fontsize=20)
            plt.text(0.05, 0.85,
                     (f"last data request:\n{dataPlots['dt']}\n"
                      "data source:\nhttps://covid2019-api.herokuapp.com/"),
                     transform=ax.transAxes,
                     bbox=dict(facecolor='grey',
                               alpha=0.5),
                     fontsize=18)
            plt.legend(fontsize=18)
            plt.grid()
            plt.tight_layout()
            plt.savefig(f'plots/{country.replace("*", "")}.png')
            plt.cla()   # Clear axis
            plt.clf()   # Clear figure
            plt.close()
            logger.info(f'create {country} plot')
            # plt.show()
