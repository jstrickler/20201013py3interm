#  Copyright (c) 2020. CJ Associates

class HtmlWrapper:

    def __init__(self, tag):
        self._tag = tag

    def __call__(self, s):
        return "<{0}>{1}</{0}".format(self._tag, s)

    def get_tag(self):
        return self._tag

    @property
    def tag(self):
        return self._tag

h1 = HtmlWrapper('h1')

print(h1("Wombats for Fun and Profit"))

div = HtmlWrapper('div')
print(div("First part"))

print(div.get_tag())
print(h1.tag)
