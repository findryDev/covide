import htmlLinux
import httpd

import sys
import os
import shutil

import time
import datetime as dt

import requests
import json

import pandas as pd
import matplotlib.pyplot as plt

def ifDateChange():
    with open('dateLoad.txt', 'r+') as f:
        data = f.read()

    if dt.datetime.now() != dt.datetime.strptime(data, r'%m/%d/%y'):
        print('data ok')
    else:
        while True:
            if dt.datetime.now() == dt.datetime.strptime(date, r'%m/%d/%y'):
                print('Wait to change data')
                time.sleep(60)
                continue
            else:
                print('data ok')
                break


def WaitTime(timeStart):

    startDate = dt.datetime(day=dt.datetime.now().day, month=dt.datetime.now().month, year=dt.datetime.now().year, hour=timeStart)

    n = dt.datetime.now()

    if int((startDate - n).total_seconds()) < 0:
        return int((startDate - n).total_seconds()) + 24 * 60 * 60
    elif int((startDate - n).total_seconds()) > 0:
        return int((startDate - n).total_seconds())
    else:
        return 0


def writeLog(file, text):
    with open(file, 'a+') as f:
        f.write(text + '\n')
        print(text)

def make_csv():

    mainPath = ''

    try:
        c = requests.get('https://covid2019-api.herokuapp.com/timeseries/confirmed')
        if c != '200':
            with open('dateLoad.txt' , 'w+') as f:
                f.write(json.loads(c.text)['dt'])
            shutil.rmtree(mainPath + 'date/')
            print('delete date dir')
            shutil.rmtree(mainPath + 'max/')
            print('delete max dir')

            os.mkdir(mainPath + 'date/')
            print('create date dir')
            os.mkdir(mainPath + 'max/')
            print('create max dir')
            country_list = []
            # list of dictionery_confirm
            l_c = c.json()["confirmed"]
            for i in l_c:
                if i['Province/State'] == '':
                    i['country'] = i['Country/Region']
                if i['Province/State'] != '':
                    i['country'] = i['Province/State'] + '_' + i['Country/Region']
                country_list.append(i['country'])
                del i['Province/State']
                del i['Country/Region']
                del i['Lat']
                del i['Long']

            # list of dictionery_deaths
            d = requests.get('https://covid2019-api.herokuapp.com/timeseries/deaths')
            l_d = d.json()["deaths"]
            for i in l_d:
                if i['Province/State'] == '':
                    i['country'] = i['Country/Region']
                if i['Province/State'] != '':
                    i['country'] = i['Province/State'] + '_' + i['Country/Region']
                del i['Province/State']
                del i['Country/Region']
                del i['Lat']
                del i['Long']

            # list of dictionery_recovered
            r = requests.get('https://covid2019-api.herokuapp.com/timeseries/recovered')
            l_r = r.json()["recovered"]
            for i in l_r:
                if i['Province/State'] == '':
                    i['country'] = i['Country/Region']
                if i['Province/State'] != '':
                    i['country'] = i['Province/State'] + '_' + i['Country/Region']

                del i['Province/State']
                del i['Country/Region']
                del i['Lat']
                del i['Long']

            # all_dictinery:

            all_date_dict = {}
            for c in l_c:
                all_date_dict[c['country']] = {}
                all_date_dict[c['country']]['confirm'] = {}
                last = 0
                for k in c:
                    if k != 'country':
                        all_date_dict[c['country']]['confirm'][k] = int(c[k]) - last
                        last = int(c[k])

            for d in l_d:
                all_date_dict[d['country']]['deaths'] = {}
                last = 0
                for k in d:
                    if k != 'country':
                        all_date_dict[d['country']]['deaths'][k] = int(d[k]) - last
                        last = int(d[k])

            for r in l_r:
                try:
                    all_date_dict[r['country']]['recovered'] = {}
                    last = 0
                    for k in r:
                        if k != 'country':
                            all_date_dict[r['country']]['recovered'][k] = int(r[k]) - last
                        last = int(r[k])
                except:
                    continue

            with open(mainPath + 'max/max_confirm.csv', 'a+') as csvfile:
                csvfile.write('Coutry' + ':' + 'max_case_confirmed' + ':'
                + 'date_max_confirmed_case' + ':'
                + 'max_case_deaths' + ':'
                + 'date_max_deaths' + ':'
                + 'max_case_recovered' + ':'
                + 'date_max_recovered' + ':'
                + 'SUM_confirmed' + ':'
                + 'SUM_deaths' + ':'
                + 'SUM_recovered'
                + '\n')
                print('Create max file')

            for c in country_list:
                if "confirm" in all_date_dict[c]:
                    date_max_confirmed_case = max(all_date_dict[c]['confirm'], key=all_date_dict[c]['confirm'].get)
                    max_case_confirmed = all_date_dict[c]['confirm'][date_max_confirmed_case]
                else:
                    date_max_confirmed_case = '---'
                    max_case_confirmed = '---'
                    SUM_confirmed = '---'

                if "deaths" in all_date_dict[c]:
                    date_max_deaths_case = max(all_date_dict[c]['deaths'], key=all_date_dict[c]['deaths'].get)
                    max_case_deaths = all_date_dict[c]['deaths'][date_max_deaths_case]
                else:
                    date_max_deaths_case = '---'
                    max_case_deaths = '---'
                    SUM_deaths = '---'

                if "recovered" in all_date_dict[c]:
                    date_max_recovered_case = max(all_date_dict[c]['recovered'], key=all_date_dict[c]['recovered'].get)
                    max_case_recovered = all_date_dict[c]['recovered'][date_max_recovered_case]
                else:
                    date_max_recovered_case = '---'
                    max_case_recovered = '---'
                    SUM_recovered = '---'

                if "confirm" in all_date_dict[c]: SUM_confirmed = sum(all_date_dict[c]['confirm'].values())
                if "deaths" in all_date_dict[c]: SUM_deaths = sum(all_date_dict[c]['deaths'].values())
                if "recovered" in all_date_dict[c]: SUM_recovered = sum(all_date_dict[c]['recovered'].values())

                with open(mainPath + 'max/max_confirm.csv', 'a+') as csvfile:
                    csvfile.write(c + ':' + str(max_case_confirmed) + ':'
                    + str(date_max_confirmed_case) + ':'
                    + str(max_case_deaths) + ':'
                    + str(date_max_deaths_case) + ':'
                    + str(max_case_recovered) + ':'
                    + str(date_max_recovered_case) + ':'
                    + str(SUM_confirmed) + ':'
                    + str(SUM_deaths) + ':'
                    + str(SUM_recovered)
                    + '\n')
                    print(f'append max file. Country: {c}')
                if '*' in c:
                    country = c.replace('*', '')
                else:
                    country = c

                with open(mainPath + f'date/{country}.csv', 'a+') as csvfile:
                    csvfile.write('Date' + ':'
                    + 'Confirmed_case' + ':'
                    + 'Deaths_case' + ':'
                    + 'Recovered_case'
                    + '\n')
                    print(f'Create country file. Country: {country}.csv')
                    print(mainPath + f'date/{country}.csv')
                for k in all_date_dict[c]['confirm']:
                    if 'confirm' in all_date_dict[c]:
                        csv_date = k
                        csv_confirm = str(all_date_dict[c]['confirm'][k])
                    else:
                        csv_date = '---'
                        csv_confirm = '---'

                    if 'deaths' in all_date_dict[c]:
                        csv_deaths = str(all_date_dict[c]['deaths'][k])
                    else:
                        csv_deaths = '---'

                    if 'recovered' in all_date_dict[c]:
                        csv_recovered = str(all_date_dict[c]['recovered'][k])
                    else:
                        csv_recovered = '---'

                    with open(mainPath + f'date/{country}.csv', 'a+') as csvfile:
                        csvfile.write(csv_date + ':'
                        + csv_confirm + ':'
                        + csv_deaths + ':'
                        + csv_recovered
                        + '\n')
                        print(f'append country value. Country: {country}')
                        print(mainPath + f'date/{country}.csv')

        writeLog('cli_log.txt', f'CSV OK {dt.datetime.now()}')
        return True
    except Exception as e:
        writeLog('cli_log_err.txt', f'{e} {dt.datetime.now()}')
        print(e)
        return False


def make_plots():
    mainPath = ''
    country_list = []
    try:
        with os.scandir(mainPath + 'date/') as entries:
            for entry in entries:
                if entry.is_file() and entry.name.endswith('.csv') and entry.name != 'max_confirm.csv':
                    country_list.append(entry.name)

            for country in country_list:
                d = pd.read_csv(mainPath + f'date/{country}',
                                sep=':', usecols=['Date', 'Confirmed_case', 'Deaths_case', 'Recovered_case'],
                                index_col='Date')
                print('open csv file: ' + mainPath + f'date/{country}')

                dd = d[d.index.get_loc(d[d['Confirmed_case'].ge(1)].index[0]):]
                myDpi = 10
                figure = plt.figure(figsize=(50,5))
                plt.subplot(133)
                plt.plot(dd['Confirmed_case'], label='confirm')
                plt.plot(dd['Deaths_case'], label='deaths')
                plt.plot(dd['Recovered_case'], label='recovered')

                plt.legend()
                plt.title(f'Covid_{country}')
                plt.xlabel('date')
                plt.ylabel('case')
                plt.tick_params('x', labelrotation=90)
                plt.minorticks_on()
                plt.grid(which='both')
                plt.tight_layout()
                c = country.split('.')[0]
                plt.savefig(mainPath + f'plots/{c}.png', dpi=figure.dpi, bbox_inches='tight',
                            pad_inches=0.5)
                print(f'Plot country {country} save: ' + mainPath + f'plots/{c}.png')
                plt.close(figure)
        writeLog('cli_log.txt', f'PLOTS OK {dt.datetime.now()}')
        return True
    except Exception as e:
        writeLog('cli_log_err.txt', f'{e} {dt.datetime.now()}')
        print(e)
        return False


def mainLoop():
    sh = 6

    print(f'Wait  {dt.datetime.now().time()}')
    writeLog('cli_log.txt', f'Wait  {dt.datetime.now().time()}')
    for i in range(WaitTime(sh), 1, -1):
        print(f'Time to start {i}s')
        time.sleep(1)
    ifDateChange()

    print(f'Start script {dt.datetime.now()}')
    writeLog('cli_log.txt', f'Start script {dt.datetime.now()}')

    try:

        while True:
            writeLog('cli_log.txt', f'Start {dt.datetime.now()}')
            print(f'Start {dt.datetime.now()}')
            if make_csv():
                if make_plots():
                    writeLog('cli_log.txt', f'Stop {dt.datetime.now()}')
                    print(f'Stop {dt.datetime.now()}')
                    if htmlLinux.htmlMaker():
                        writeLog('cli_log.txt', f'HTML OK {dt.datetime.now()}')
                        httpd.restart()
                        writeLog('cli_log.txt', f'APACHE RESTART {dt.datetime.now()}')
                    for i in range(WaitTime(sh), 1, -1):
                        print(f'Time to start {i}s')
                        time.sleep(1)
    except Exception as e:
        writeLog('cli_log_err.txt', f'{e} {dt.datetime.now()}')
        print(e)
        for i in range(WaitTime(sh), 1, -1):
            print(f'Time to start {i}s')
            time.sleep(1)

def mainNow():
    try:
        writeLog('cli_log.txt', f'Start {dt.datetime.now()}')
        if make_csv():
            if make_plots():
                writeLog('cli_log.txt', f'Stop {dt.datetime.now()}')
                if htmlLinux.htmlMaker():
                    writeLog('cli_log.txt', f'HTML OK {dt.datetime.now()}')
                    httpd.restart()
                    writeLog('cli_log.txt', f'APACHE RESTART {dt.datetime.now()}')
    except Exception as e:
        writeLog('cli_log_err.txt', f'{e} {dt.datetime.now()}')


if len(sys.argv) > 1 and sys.argv[1] == 'now':
    mainNow()
else:
    if __name__ == '__main__': mainLoop()

