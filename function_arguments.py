
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
spam("a", "b", "c")

args = [10, 20, 30]

spam(*args)  # converts iterable into separate arguments

