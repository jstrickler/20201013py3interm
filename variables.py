from pprint import pprint

x = 5   #  create an object of type int with value 5 and assign the name 'x' to it
y = 10

result = x + y

print(result)

for i in range(3):   # implicit assignment to i of next value from range(3)
    # i = next(range(3))
    print(i)

a = x   # assigns 'a' to same object as 'x'

print(x, a)

# every object has: value, type, ID
print(x, type(x), id(x))
print(a, type(a), id(a))
print()

a = 10  # create obj, assign label 'a'

print(x, type(x), id(x))
print(a, type(a), id(a))
print()

x = 50

m = [1, 2, 3]
n = m

n.append(5)
print(m, n)


thing1 = None
thing2 = None

print(thing1, type(thing1), id(thing1))
print(thing2, type(thing2), id(thing2))
print(None, type(None), id(None))

if thing1 == None:
    print("equal to None")

if thing1 is None:  # T if two things have the same ID
    print("is None")

print([1,2,3] == [1,2,3])
print([1,2,3] is [1,2,3])
print('-' * 60)

a = [1, 2, 3, ['a', 'b', 'c']]
b = a    #  reference (alias)
c = list(a)  #  shallow copy
import copy
d = copy.deepcopy(a)   # deep copy
for obj in a, b, c, d:
    print(obj, id(obj))
print('-' * 60)
c[3].append("wombat")
d[3].append("wolverine")
for obj in a, b, c, d:
    print(obj, id(obj))


people = ['Fred', 'Eliza', 'Bette']

def doit(p):
    p.append("Mary")

doit(people)

print(people)

#   lower_case_words_with_underscores

# Numeric: bool complex int float
# Sequence (array): list str bytes tuple
# Mapping (key-oriented): dict set frozenset

i = 23582039582039582039582039582039582039582093582093850293850293850298350298350928350928
print(i)
print(i + 1)

x = 1.2394082938983e32
print(x, '\n')


#  NOPE: ++ --

# YEP:  += -+ *= %=

s1 = "hello"
s2 = b"hello"
s3 = ['h', 'e', 'l', 'l', 'o']
s4 = 'h', 'e', 'l', 'l', 'o'

for x in s1, s2, s3, s4:
    print(x, type(x), len(x), x[0], x[:2])
print()

s = 'wombat'
print(s.upper(), s.startswith('w'), s.lower().startswith('W'))

spam1 = "spam\n"
spam2 = 'spam\n'
spam3 = """spam\n"""
spam4 = '''spam\n'''

print(spam1)
print(spam2)

print(spam1 is spam2)

print("""Guido's the "BDFL" of "" '' Python""")

# print qw(Guido's the "BDFL" of "" '' Python\n);   # perl equiv

def doit():
    """
    THis is a cool function
    :return:
    """
    pass

actor = "Chris Hemsworth"

print(actor.replace('Chris', 'Liam'))   # Liam  William
print(actor.split())
print(', '.join(actor.split()))

# Topher Grace
print(actor[:5])
print(actor[-9:])

# S[START:STOP:STEP]


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

print(airports['YYZ'])
print(airports.get('YOW'))
print(airports.get('UVX', "HUH?"))
airports['SJO'] = "San Jose, CR"
print(airports)


pprint(airports)

  #  d1 |= d2     # NEW
  #  d1.map(d2)   # OLD


for abbr, name in airports.items():
    print(abbr, name)
print()

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

for abbr, name in sorted(airports.items(), key=lambda item: (item[1], item[0])):
    print(abbr, name)
print()

print(airports.items(), '\n')

def by_value(element):
    return element[1], element[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()

kathy_visited = ['Costa Rica', 'France', 'Portugal', 'China', 'Botswana', 'Burkina Faso']
cheryl_visited = ['France', 'Germany', 'UK', 'Italy', 'Japan', 'China']

k = set(kathy_visited)
c = set(cheryl_visited)

print("both:", k & c)
print("just one:", k ^ c)
print("all:", k | c)
print("just Kathy:", k - c)
print("just Cheryl:", c - k)

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']

print(set(food))

