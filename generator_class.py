

class Colors:

    def __init__(self, *colors):
        self._start = 0
        self._colors = colors

    def __iter__(self):
        return self

    def __next__(self):
        if self._start == len(self._colors):
            raise StopIteration

        index = self._start
        self._start += 1

        return self._colors[index]

if __name__ == '__main__':

    c = Colors("red", "green", "purple")

    for color in c:
        print(color)
    print()

    c = Colors("brown", "orange", "black")

    print(next(c))
    print(next(c))
    print(next(c))

    with open('DATA/mary.txt') as mary_in:
        headers = next(mary_in)
        for line in mary_in:
            print(line.rstrip())



