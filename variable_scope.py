import sys

MAX_TRIES = 5  # global variable

# def print(*args):
#     sys.stdout.write("HA HA HA!\n")

def doit():
#    global animal  # VERY VERY NAUGHTY
    animal = 'wombat'   # local variable
    print("max tries:", MAX_TRIES)

    return animal


x = doit()

print("animal is", x)

# local -> nonlocal -> global -> builtin

def spam():
    x = 5  # local to spam(), nonlocal to ham()

    def ham():
        print("in ham(): x is", x)

    print("in spam(): ham id is", id(ham))
    return ham

f = spam()
f()
print("in main: f id is", id(f))

print(f, spam, print)
