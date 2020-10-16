#  Copyright (c) 2020. CJ Associates
from threading import Thread, Lock
from random import randint
import time

screen_lock = Lock()

def the_work(num):
    time.sleep(randint(1, 3))
    with screen_lock:
        print(f"Num is {num}")

for i in range(10):
    t = Thread(target=the_work, args=(i,))
    t.start()

print("All threads launched")
