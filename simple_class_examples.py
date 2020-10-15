from datetime import date


pearl_harbor = date(1941, 12, 7)

print(pearl_harbor)

x = 5   #   x = int(5)

class Dog:
    def __init__(self, name):
        self.dog_name = name  # will use the setter property

    def bark(self):
        print("Woof! Woof!")

# property == managed attribute

    @property
    def dog_name(self):  # getter property
        return self._name
        # look up DB ID in DB

    @dog_name.setter
    def dog_name(self, name):
        # put name DB
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("Dog name must be a string")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

d = Dog("Andy")
d.bark()
print(type(d))
print(d)

print(d.dog_name)

d2 = Dog("Nellie")
d2.bark()
print(d2.dog_name)   #  NOT d2.name()

try:
    d3 = Dog(123.456)
except TypeError as err:
    print(err)
else:
    print(d3.dog_name)

d.dog_name = "Scooby-Doo"  #  Dog.dog_name(d, "Scooby-Doo")
print(d.dog_name)

print(d.get_name())

d.breed = "English Shepherd"

print(d.breed)

d.breed = "Martian Hogboggler"
d.breed = 98302

