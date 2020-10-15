
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1", f1, "\n")

f2 = sorted(fruits, key=str.lower)
print("f2", f2, "\n")

f3 = sorted(fruits, key=len)
print("f3", f3, "\n")

def len_and_name(f):
    return len(f), f.lower()

f4 = sorted(fruits, key=len_and_name)
print("f4", f4, "\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for first_name, last_name, product, dob in sorted(people):
    print(first_name, last_name, product, dob)
print('-' * 60)

def by_ln_fn(person):
    return person[1], person[0]

for first_name, last_name, product, dob in sorted(people, key=by_ln_fn):
    print(first_name, last_name, product, dob)
print('-' * 60)

for first_name, last_name, product, dob in sorted(people, key=lambda p: (p[1], p[0])):
    print(first_name, last_name, product, dob)
print('-' * 60)

# lambda param, ...: return-value



