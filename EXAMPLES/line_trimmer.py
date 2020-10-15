#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')


for line in trimmed('../DATA/mary.txt'):  # <2>
    print(line)
