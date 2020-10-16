#  Copyright (c) 2020. CJ Associates
import lxml.etree as ET

doc = ET.parse('computer_people.xml')

root = doc.getroot()

class Person:
    def __init__(self, person_element):
        pass

for person in root:
    # p = Person(person)
    # print(p.first_name)
    first_name = person.findtext('firstname')
    last_name = person.findtext('lastname')
    print(first_name, last_name)

# people = [Person(p) for p in root]
