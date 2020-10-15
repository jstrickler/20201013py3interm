#!/usr/bin/env python

import re

with open("../DATA/alice.txt") as mary_in:
    s = {w.lower()  for ln in mary_in  for w in re.split(r'\W+', ln) if w} #<1>
print(sorted(s))
