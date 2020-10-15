"""
Provide CardDeck class
"""
import random

class CardDeck:
    """
    One deck of cards
    """
    SUITS = "Clubs Diamonds Hearts Spades".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, dealer_name):
        self.dealer_name = dealer_name
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    def shuffle(self):
        """
        Randomize the deck

        :return:
        """
        random.shuffle(self._cards)

    def draw(self):
        """
        Retrieve a card from the deck

        :return:
        """
        return self._cards.pop()

    @property
    def cards(self):
        """
        List of current cards in deck

        :return:
        """
        return self._cards

    @property
    def dealer_name(self):
        """
        Get/set dealer name

        :return:
        """
        return self._dealer_name

    @dealer_name.setter
    def dealer_name(self, value):
        if isinstance(value, str):
            self._dealer_name = value
        else:
            raise TypeError("Dealer must be a string")


    @classmethod
    def get_ranks(cls):
        """
        Return list of card ranks

        :return:
        """
        return cls.RANKS

    @staticmethod
    def yell():
        """Silly method"""
        print("HOORAY!!!")

    def __len__(self):  # implements len()
        return len(self._cards)

    # the string version of an object should be human-friendly
    def __str__(self):  # implements  str()
        my_class = type(self)  # class of current objct
        my_name = my_class.__name__
        return f"{my_name}({self.dealer_name}, {len(self)})"

    # code-friendly
    def __repr__(self): # how the object is/was created in code
        my_class = type(self)  # class of current objct
        my_name = my_class.__name__
        return f"""{my_name}("{self.dealer_name}")"""

    def __add__(self, other):
        tmp = type(self)(self.dealer_name)
        tmp._cards = self.cards + other.cards
        return tmp
