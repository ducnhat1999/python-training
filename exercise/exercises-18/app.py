import random
from re import S
from sys import prefix

class Card:
  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

  def __init__(self, suit=0, rank=2):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

  def __lt__(self, other):
    t1 = self.suit, self.rank
    t2 = other.suit, other.rank
    return t1 < t2

class Deck:
  def __init__(self):
    self.cards = []
    for suit in range(4):
      for rank in range(1, 14):
        card = Card(suit, rank)
        self.cards.append(card)
  def __str__(self):
    result = []
    for card in self.cards:
      result.append(str(card))
    return '\n'.join(result)

  def add_card(self, card):
    self.cards.append(card)

  def pop_card(self):
    return self.cards.pop()

  def suffle(self):
    random.shuffle(self.cards)

  def sort(self):
    self.cards.sort()

  def move_cards(self, hand, num):
    for i in range(num):
      hand.add_card(self.pop_card())

class Hand(Deck):
  def __init__(self, label=""):
    self.cards = []
    self.label = label

class Markov:
  def __init__(self):
    self.suffix_map = {}
    self.prefix = ()
  def process_word(self, word, order=2):
    if len(self.prefix) < order:
      self.prefix += (word,)
      return

    try:
      self.suffix_map[self.prefix].append(word)
    except KeyError:
      self.suffix_map[self.prefix] = [word]

    self.prefix = shift(self.prefix, word)


queen_of_diamonds = Card(1, 12)
card1 = Card(3, 5)

# print(queen_of_diamonds < card1)
# print(time1 < time2)
deck = Deck()
deck.suffle()
deck.sort()
# print(deck)

hand = Hand("new hand")
print(hand.label)
card = deck.pop_card()
hand.add_card(card)
print(hand)
deck.move_cards(hand, 5)
print(hand)