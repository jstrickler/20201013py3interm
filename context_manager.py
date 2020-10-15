

with open('DATA/mary.txt') as mary_in:
    pass


class Spam:
    def __init__(self):
        print("in constructor")
        self.color = 'blue'

    def __enter__(self):
        print("Entering with block")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exiting with block")
        # e.g., self.close()



with Spam() as s:  #  s = Spam()
    print("In the with block")
