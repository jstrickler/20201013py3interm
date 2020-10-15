#  Copyright (c) 2020. CJ Associates
from collections import namedtuple

thing = 5, "wombat", 8.9

print(thing[0], thing[2])

Thing = namedtuple('Thing', 'repeat_count animal fudge_factor')

t1 = Thing(5, "wombat", 8.9)

print(t1.animal, t1.fudge_factor)
print(t1.repeat_count)

print(Thing.__name__)
