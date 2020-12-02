import requests
import json
import cov.htmlLinux


r = requests.get('https://covid2019-api.herokuapp.com/countries')
j = json.loads(r.text)

countries = j["countries"]
countries = [country.replace('_', ' ') for country in countries]
countries = [country.replace('US', 'United States') for country in countries]


r = requests.get('https://flagcdn.com/en/codes.json')
countryISO = json.loads(r.text)
countryISO = {value: key for key, value in countryISO.items()}
notCountry = []

for country in countries:
    try:
        if country in countryISO.keys():
            r = requests.get(f'https://flagcdn.com/256x192/{countryISO[country]}.png')
            with open(f'flags/{country}.png', 'wb') as f:
                f.write(r.content)
        else:
            notCountry.append(country)
    except Exception as e:
        print(e)
        notCountry.append(country)
        continue


print(notCountry)
print(countryISO)
