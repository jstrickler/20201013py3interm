

x = ['a', 'b', 'c']

for letter in x:  # x is an iterable
    # letter = next value of x
    print(letter)
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

start = 'x'
for f in fruits:
    if f.lower().startswith(start):
        print(f)
        break
else:
    print("Not found")
