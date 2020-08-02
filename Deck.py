from const import SUITS,RANKS,PRINTED

from itertools import product
from random import shuffle


class Card:
    def __init__(self,suit,rank,picture,points):
        self.suit = suit
        self.picture = rank
        self.picture = picture
        self.points = points


    def __str__(self):
        message = self.picture + 'Points: '+ str(self.points)







class Deck:

    def __init__(self):
        self.cards=self._create_deck()
        shuffle(self.cards)


    def _create_deck(self):
        cards = []
        for suit,rank in product(SUITS,RANKS):
            if rank =='ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            picture = PRINTED.get(rank)

            c = Card (suit=suit,rank=rank,points=points,picture=picture)

            cards.append(c)
        return cards


    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


