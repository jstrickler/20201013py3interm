#!/usr/bin/env python
#
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):  # <1>

    @abstractmethod   # <2>
    def speak(self):
        """
        This is how you should implement this method...

        :return:
        """
        pass

    def run(self):
        print("I'm running...")

class Dog(Animal):  # <3>
    def speak(self):   # <4>
        print("woof! woof!")

class Cat(Animal):  # <3>
    def speak(self):  # <4>
        print("Meow meow meow")

class Duck(Animal): # <3>
    def quack(self):
        print("quack quack quack")# <5>

d = Dog()
d.speak()
d.run()

c = Cat()
c.speak()

try:
    d = Duck()  # <6>
    d.speak()
except TypeError as err:
    print(err)
