'''
this class will add card to deck
'''

from random import shuffle
from card_module import Card
class Deck():
    suits = ('spades♤', 'hearts♡', 'diamonds◇', 'clubs♧')
    ranks = (
        'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
        'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack'
        )

    def __init__(self) -> None:
        self.all_cards = []

        for suit in self.suits:
            for rank in self.ranks:
                self.all_cards.append(Card(suit, rank))

    def deal_card(self):
        return self.all_cards.pop(0)
    
    def shuffle(self):
        shuffle(self.all_cards)

    def split_cards_by_players(self, player_one, player_two):
        for i in range (0, len(self.all_cards)):
            if i % 2 == 0:
                player_one.add_cards(self.all_cards[i])
            else: 
                player_two.add_cards(self.all_cards[i])