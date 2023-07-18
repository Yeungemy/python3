'''
this class will hold 52 cards 
'''
suits = ('spades♤', 'hearts♡', 'diamonds◇', 'clubs♧')
ranks = (
    'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
    'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack'
    )


from random import shuffle
from card import Card
class Deck():
    def __init__(self) -> None:
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    def __str__(self) -> str:
        deckCom = ''
        for card in self.all_cards:
            deckCom += card.__str__() + '\n'
        return deckCom
    
    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)