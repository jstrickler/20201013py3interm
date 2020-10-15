

class Spam():
    def foo(self):
        pass

    def bar(self):
        pass


class Ham():
    def blah(self):
        pass

    def baz(self):
        pass

class Toast():
    def buttered(self):
        pass


class A(Spam, Ham):
    pass

class B(Ham, Toast):
    pass

class C(Toast, Spam)
    pass
