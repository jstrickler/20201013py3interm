
t = 5, 8, "wombat"

print(t, type(t), len(t))

print(t[0], t[1], t[-1], t[:2])

person = "Bill", "Gates", "Microsoft", '10-28-55'

print(person[2])

first_name, last_name, *product, dob = person  # iterable unpacking

print(first_name, last_name)

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'NeXt', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
    ('Joe', 'Schmoe', '1982-6-14'),
]

print(people[0])
print(people[0][0])
print(people[0][0][0])

# for first_name, last_name, product, dob in people:
#     print(first_name, last_name, product)
# print('-' * 60)

for first_name, last_name, *product, dob in people:
    # first_name, last_name, *product, dob = <next element of people>
    print(first_name, last_name, product)
print('-' * 60)

for i, value in enumerate(values):
    print(i, value)
print('-' * 60)

print(list(enumerate(values)))

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for abbr, airport in airports.items():
    print(abbr, airport)
print('-' * 60)

print(airports.items())


