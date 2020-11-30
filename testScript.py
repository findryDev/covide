import requests
import json
import cov.htmlLinux


r = requests.get('https://covid2019-api.herokuapp.com/countries')
j = json.loads(r.text)

countries = j["countries"]
countries = [country.replace('_', ' ') for country in countries]

r = requests.get('https://flagcdn.com/en/codes.json')
countryISO = json.loads(r.text)
countryISO = {value: key for key, value in countryISO.items()}
restCountry = []

for country in countries:
    if country in countryISO.keys():
        r = requests.get(f'https://flagcdn.com/256x192/{countryISO[country]}.png')
        with open(f'flags/{country}.png', 'wb') as f:
            f.write(r.content)
    else:
        restCountry.append(country)

print(restCountry)
