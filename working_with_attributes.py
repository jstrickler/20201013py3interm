#  Copyright (c) 2020. CJ Associates
from president import President
import datetime
import inspect as ins

p = President(26)

print(p)
print(p.first_name)
print(p.last_name, '\n')

attr = "first_name"

print(getattr(p, attr))

d = getattr(datetime, 'date')

today_func = getattr(d, 'today')
today = today_func()

print(today)

print(hasattr(p, "spouse"))

setattr(p, 'spouse', 'Martha')

print(p.spouse)

delattr(p, 'spouse')

# delattr(p, 'party')

print(p.__dict__)

print(dir(p))

print("ATTRIBUTES:")
for attr in dir(p):
    if not attr.startswith('__'):
        obj = getattr(p, attr)
        print(attr, str(obj)[:30], type(obj), ins.isfunction(obj), ins.ismodule(obj))
print()

print(dir(__builtins__))

# def print(*args):  # weird and confusing
#     pass
#
# __builtins__.print("Hello")

def mfn(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, 'get_fullname', mfn)


print(p.get_fullname())

