#!/usr/bin/env python
from multiprocessing import Pool, Manager  # <1>
from pprint import pprint
import requests

m = Manager()
values = m.list()
other_values = m.dict()


POOL_SIZE = 64

BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # <2>

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # <3>

search_terms = open('../DATA/words.txt').read().splitlines()

def fetch_data(term):  # <5>
    try:
        response = requests.get(
            BASE_URL + term,
            params={'key': API_KEY},
        )  # <6>
    except requests.HTTPError as err:
        print(err)
        return []
    else:
        data = response.json()  # <7>
        parts_of_speech = []
        for entry in data: # <8>
            if isinstance(entry, dict):
                meta = entry.get("meta")
                if meta:
                    part_of_speech = entry.get("fl")
                    if part_of_speech:
                        parts_of_speech.append(part_of_speech)
        return sorted(set(parts_of_speech))  # <9>


if __name__ == '__main__':

    p = Pool(POOL_SIZE)  # <10>

    results = p.map(fetch_data, search_terms[:1000])  # <11>

    for i, (search_term, result) in enumerate(zip(search_terms, results)):  # <12>
        print("{}:".format(search_term.upper()), end=' ')
        if result:
            print(result)
        else:
            print("** no results **")
        print()
        if i == 10:
            break
