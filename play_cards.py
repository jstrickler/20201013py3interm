from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Mary")
print(d1.dealer_name)
print(d1)

d1.dealer_name = "Ernesto"
#  d1.shuffle() d1.draw()

print(d1.dealer_name)

d1.shuffle()
print(d1.cards)

print()
for i in range(5):
    print(d1.draw())
print()

print(d1.get_ranks())
print(CardDeck.get_ranks())

CardDeck.yell()
d1.yell()

j1 = JokerDeck("Ally")
print(j1)  # print(str(j1))
j1.shuffle()
print(j1.cards)

print(CardDeck.mro())
print(JokerDeck.mro())

print(len(d1), len(j1))

print(repr(d1), repr(j1))

new_deck = d1 + j1

print(new_deck)
new_deck.shuffle()

from pathlib import Path

p1 = Path("Data")
p2 = Path("alice.txt")

path = p1 / p2
print(path)

