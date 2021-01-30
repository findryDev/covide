import requests
import json
import os


def getFlags():
    countries = []
    for _, _, files in os.walk('plots'):
        for name in files:
            if name == 'US': name = 'United States'
            try:
                if ' - ' in name: name = name.split(' - ')[1]
            except Exception as e:
                print(e, name)
            countries.append(name.split('.')[0])

    r = requests.get('https://flagcdn.com/en/codes.json')
    countryISO = json.loads(r.text)
    countryISO = {value: key for key, value in countryISO.items()}
    notCountry = []

    for country in countries:
        try:
            if country in countryISO.keys():
                r = requests.get(f'https://flagcdn.com/256x192/{countryISO[country]}.png')
                with open(f'flags/{country.replace(" ", "_")}.png', 'wb') as f:
                    f.write(r.content)
                print(country)
            elif country.split("-")[1] in countryISO.keys():
                r = requests.get(f'https://flagcdn.com/256x192/{countryISO[country.split("-")[1]]}.png')
                with open(f'flags/{country.split("-")[1]}.png', 'wb') as f:
                    f.write(r.content)
                print(country.split("-")[1])
                r = requests.get(f'https://flagcdn.com/256x192/{[country.split("-")[0]]}.png')
                with open(f'flags/{country.split("-")[0]}.png', 'wb') as f:
                    f.write(r.content)
                print(country.split("-")[0])
            else:
                notCountry.append(country)
        except Exception as e:
            print(e, country)
            notCountry.append(country)
            continue


def flag_compare():
    plotsFiles = []
    flagsFiles = []

    for _, _, files in os.walk('plots'):
        for name in files:
            plotsFiles.append(name)

    for _, _, files in os.walk('flags'):
        for name in files:
            flagsFiles.append(name)

    for f in plotsFiles:
        if f not in flagsFiles:
            print(f)

    print(20* '_')
    i = 0
    for f in plotsFiles:
        try:
            if f.split(' - ')[1] not in flagsFiles:
                print(f)
                i += 1
        except:
            print('...')

    print(i)



r = requests.get('https://flagcdn.com/en/codes.json')
countryISO = json.loads(r.text)
countryISO = {value: key for key, value in countryISO.items()}

getFlags()