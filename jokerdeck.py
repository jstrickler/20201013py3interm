
from carddeck import CardDeck

class MotherOfThing:
    pass

class Thing(MotherOfThing):

    def doit(self):
        print("I am a Thing()!!!")


class JokerDeck(Thing, CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call method in base class
        self._cards.append(('Joker', 1))
        self._cards.append(('Joker', 2))



