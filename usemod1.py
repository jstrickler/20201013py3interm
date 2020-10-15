#!/usr/bin/env python

# from pkg.pkg.pkg import module
from cja.db.utils import mymod  # find cja/db/utils/mymod.py in PYTHONPATH

#  sys.path

mymod.spam()
mymod.ham()

# mymod._toast()  # NAUGHTY!!
print(mymod, id(mymod))


print(mymod.ANIMALS)

t = mymod.Thing()
print(t, '\n')

import sys
for path in sys.path:
    print(path)
