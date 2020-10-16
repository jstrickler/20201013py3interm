#  Copyright (c) 2020. CJ Associates
from threading import Thread, Lock
from random import randint
import time

screen_lock = Lock()
values_lock = Lock()

values = []

class Demo(Thread):

    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        time.sleep(randint(1, 3))
        with values_lock:
            values.append(self.num)

        with screen_lock:
            print(f"Num is {self.num}")

thread_list = []
for i in range(10):
    t = Demo(i)
    t.start()
    thread_list.append(t)

print("All threads launched")
for t in thread_list:
    t.join()  # wait for thread to finish

print("values:", values)
