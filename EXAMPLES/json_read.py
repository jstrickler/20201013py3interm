#!/usr/bin/env python

import json

with open('../DATA/solar.json') as solar_in:  # <1>
    solar = json.load(solar_in)  # <2>  # build python data structure from the JSON string

# json.loads(STRING)
# json.load(FILE_OBJECT)

# print(solar)

print(solar['innerplanets'])  # <3>
print('*' * 60)
print(solar['innerplanets'][0]['name'])
print('*' * 60)
for planet in solar['innerplanets'] + solar['outerplanets']:
    print(planet['name'])

print("*" * 60)
for group, planets in solar.items():
    if group.endswith('planets'):
        for planet in planets:
            print(planet['name'])
