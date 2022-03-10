import random

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

  def deal_hands(self, n_hands, cards_hand):
    cards_of_hands = {}
    for i in range(n_hands-1):
      cards = []
      for n_card in range(cards_hand-1):
        suit = random.randint(1,3)
        rank = random.randint(1,13)
        card = Card(suit, rank)
        cards.append(card)
      cards_of_hands['hand%d' % (i)] = cards
    return cards_of_hands
      


class Hand(Deck):
  def __init__(self, label=""):
    self.cards = []
    self.label = label

deck = Deck()
cards_of_hands = deck.deal_hands(4, 6)
for hand in cards_of_hands:
  print(hand)
  for card in cards_of_hands[hand]:
    print(card)