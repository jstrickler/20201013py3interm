#!/usr/bin/env python
# (c) 2015 John Strickler
#
import sys
from datetime import date
import yaml

potus = {
    1: {
        'lname': 'Washington',
        'fname': 'George',
        'dob': date(1732, 2, 22),
        'dod': date(1799, 12, 14),
        'birthplace': 'Westmoreland County',
        'birthstate': 'Virginia',
        'term': [ date(1789, 4, 30), date(1797, 3, 4) ],
        'assassinated': False,
        'party': None,
    },
    2: {
        'lname': 'Adams',
        'fname': 'John',
        'dob': date(1735, 10, 30),
        'dod': date(1826, 7, 4),
        'birthplace': 'Braintree, Norfolk',
        'birthstate': 'Massachusetts',
        'term': [date(1797, 3, 4), date(1801, 3, 4)],
        'assassinated': False,
        'party': 'Federalist',

    },
}

with open('potus.yaml', 'w') as potus_out:
    yaml.dump(potus, potus_out)

yaml.dump(potus, sys.stdout)
