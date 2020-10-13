
i = 0
while i < 3:
    print(i)
    i += 1
print()

for i in range(3):
    print(i)
print()

while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    if name =='':
        continue
    print(f"Welcome, friend {name}")   # modern man
    print("Welcome, friend {}".format(name))   # neanderthal
    print("Welcome, friend %s" % (name))   # australopithecus

print(f"Answer is {2 + 2}")

