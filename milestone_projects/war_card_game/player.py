'''
This class create a player object 
'''

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.all_cards = []

    def __str__(self) -> str:
        return f'{self.name} has {len(self.all_cards)}'
    
    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def remove_cards(self, number_of_cards):
        removed_cards = []

        for i in range(0, number_of_cards):
            removed_cards.append(self.remove_card())
        
        return removed_cards
