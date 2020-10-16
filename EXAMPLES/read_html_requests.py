#!/usr/bin/env python

import requests

response = requests.get("https://www.python.org")  # <1>

if response.status_code == requests.codes.OK:

    for header, value in sorted(response.headers.items()): # <2>
        print(header, value)
    print()

    print(response.content[:1000].decode())   # <3>
    print('...')
    print(response.content[-1000:].decode())   # <4>
else:
    print("Error fetching page:", response.status_code)


