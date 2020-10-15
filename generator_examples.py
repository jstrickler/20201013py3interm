
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


fgen = (f.upper() for f in fruits)

print(fgen)
print(list(fgen))

print("first time")
for fruit in fgen:
    print(fruit)
print()

print("second time:")
for fruit in fgen:
    print(fruit)
print()



ufruits = (f.upper() for f in fruits)
short_fruits = (f[:3] for f in ufruits)
xfruits = (f.replace('A', 'X') for f in short_fruits)

for fruit in xfruits:
    print(fruit)
