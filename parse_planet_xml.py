#  Copyright (c) 2020. CJ Associates
import lxml.etree as ET

doc = ET.parse('DATA/solar.xml')

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")
