#  Copyright (c) 2020. CJ Associates
import datetime
import inspect

class Spam:
    pass

def ham(p1: int, p2: str, *p3, p4: float, p5: float, **p6) -> float:
    print("Hello from ham!")
    return 3.4

toast = "rye"

eggs = 1.23

print(globals().keys())
print(globals().values())
print(globals())

g = globals()
print(g['eggs'])
g['ham'](2, 'foom', p4=1.2, p5=3.4)   # ham()

g['animal'] = 'wombat'

print(animal)

g['bark'] = lambda : print("Woof! Woof!")

bark()

def foom():
    x = 10
    y = 20
    z = "zebra"

    print("In foom(): locals are", locals())

foom()

for x in ham, datetime, Spam, toast:
    print(inspect.isfunction(x), inspect.ismodule(x), inspect.ismethod(x), inspect.isclass(x))

print(inspect.getfullargspec(ham))
