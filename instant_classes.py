#  Copyright (c) 2020. CJ Associates

class Animal:
    def run(self):
        print("running...")

class Cat(Animal):

    def meow(self):
        print("meoowwwwwwwww")

c1 = Cat()
c1.meow()

def bark(self):
    print("woof! woof!")

Dog = type('Dog', (Animal,), {'bark': bark})

d1 = Dog()
d1.bark()
d1.run()
