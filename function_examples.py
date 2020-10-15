
def get_message():
    return "Hello!"

def say_message():
    message = get_message()
    print(message)
    # return None

say_message()

def cube(x):  # parameters in function def
    return x ** 3


print(cube(5))   # arguments passed to function call
print(cube(99))

def findit(file_name, search_term):
    with open(file_name) as file_in:
        for line in file_in:
            if search_term in line:
                print(line.rstrip())

findit('DATA/mary.txt', 'lamb')
findit('DATA/alice.txt', 'Lizard')
print('-' * 60)
def findit2(*, file_name, search_term):
    with open(file_name) as file_in:
        for line in file_in:
            if search_term in line:
                print(line.rstrip())

findit2(file_name='DATA/mary.txt', search_term='lamb')
findit2(search_term="Lizard", file_name='DATA/alice.txt')

def findit3(file_name, *search_terms):
    with open(file_name) as file_in:
        for line in file_in:
            for search_term in search_terms:
                if search_term in line:
                    print(line.rstrip())

findit3('DATA/alice.txt', 'Mad', 'Lizard', 'Duchess')
findit3('DATA/alice.txt')

def config(**kwargs):
    print("kwargs:", kwargs)

config(animal="wombat", country="Burkina Faso", car="Maserati", state="Vermont")

# def spam(a, b, /, c, d):
#     print(a, b, c, d)
#

def blah(foo, bar, /):
    print(foo, bar)

blah(1, 2)
blah('spam', 'ham')

blah(bar=5, foo=88)

