#  Copyright (c) 2020. CJ Associates
from multiprocessing.dummy import Pool
from random import randint
import time

def task(num):
#    time.sleep(randint(1, 3))
    return num * 1000

input_values = range(10000000)

p = Pool(4)
output_values = p.map(task, input_values)

# print("input_values:", input_values)
# print("output_values:", output_values)
