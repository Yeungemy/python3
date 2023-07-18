'''
This class will create a single card object
'''
class Card:
    face_values = {
        'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 
        'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
        'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 
        'King': 10
        }

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.face_value = self.face_values[rank]

    def __str__(self) -> str:
        return f'suit {self.suit} of {self.rank}'