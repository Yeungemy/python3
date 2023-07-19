'''
This class hold a single card object
'''

faceValues = {
        'Two': 2, 'Three': 3, 'Four': 4, 
        'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
        'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 
        'King': 10, 'Ace': 11
        }

class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.faceValue = faceValues[rank]

    def __str__(self) -> str:
        return f'{self.suit} of {self.rank}'