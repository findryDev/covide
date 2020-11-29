import requests
import json
import cov.htmlLinux


r = requests.get('https://covid2019-api.herokuapp.com/countries')
j = json.loads(r.text)

countries = j["countries"]

r = requests.get('https://flagcdn.com/en/codes.json')
countryISO = json.loads(r.text)
countryISO = {value: key for key, value in countryISO.items()}

for key in countryISO:
    if key in countries:
        print(f'https://flagcdn.com/256x192/{countryISO[key]}.png')
        r = requests.get(f'https://flagcdn.com/256x192/{countryISO[key]}.png')
        with open(f'flags/{key}.png', 'wb') as f:
            f.write(r.content)

cov.htmlLinux.htmlMaker()