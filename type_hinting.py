#  Copyright (c) 2020. CJ Associates
import typing as T



def add(a: T.Any, b: T.Any) -> int:
    return a + b


print(add(5, 10))
print(add(.3, 99.7))
print(add('a', 'b'))
print(add([1,2,3], [4,5,6]))


class First:

    def process(self, s: 'Second'):
        pass

class Second:
    pass

Number = T.Union[int, float]

def add(a: Number, b: Number) -> Number:
    return a + b

print(add(5, 10))
print(add(.3, 99.7))
print(add('a', 'b'))
print(add([1,2,3], [4,5,6]))


def spam(things: T.Iterable[str]) -> str:
    print(things)
    return 10

spam(['a', 'b', 'c'])
spam([1, 2, 3])
g = (c.upper() for c in ('a', 'b', 'c'))

spam(g)

x: str = "Happy Halloween"

y: str = 1234

names: T.Iterable[str] = ['Bob', 'Ray', 'Sue', 'Tom']

print(type(names))

names.append('Mike')
print(names)
names.append(5)
print(names)








