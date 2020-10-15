#  Copyright (c) 2020. CJ Associates
from functools import wraps
import sys

print(sys.modules['unittest'])

def spam(a, b):
    print("Hello from spam()")
    return 100

print("spam's name is", spam.__name__)

def toast(a):
    print("Hello from toast()")
    return 1000000000000

def mydecorator(func):

    @wraps(func)  # update wrapper with properties of func
    def wrapper(*args, **kwargs):
        print("Hello from wrapper()")
        result = func(*args, **kwargs)  # calls spam(), toast(), etc.
        return result * 5

    return wrapper

spam = mydecorator(spam)
value = spam(100, 200)
print(value)
print()

print("spam's name is", spam.__name__)

toast = mydecorator(toast)
value = toast(42)
print(value)
print()

@mydecorator
def eggs(a, b, c):    #  eggs = ham(eggs)
    return "bob"

value = eggs('do', 're', 'mi')
print(value)


def doit(color, value):
    """decorator that has parameters"""
    def wrapper(func):
        """wrapper that gets the original function"""
        @wraps(func)
        def replacement(*args, **kwargs):
            """replacement function that is called when the original is called"""
            print("replacement!!")
            result = func(*args, **kwargs)
            return result
        return replacement
    return wrapper


@doit('blue', 100)
def foo():
    print("foo()")

# foo = doit('blue', 100)(foo)

foo()


@mydecorator
def bar():
    print("bar()")

# bar = mydecorator(bar)






