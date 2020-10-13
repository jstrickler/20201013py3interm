#!/usr/bin/env python
# (c) 2015 John Strickler
#
from pprint import pprint
import yaml


with open('../DATA/mongo.yaml') as mongo_in:
    mongo_data = yaml.load(mongo_in)

pprint(mongo_data)


