'''
This class create a player object 
'''

class Player:
    def __init__(self, name, round_count = 0) -> None:
        self.name = name
        self.round_count = round_count
        self.all_cards = []

    def __str__(self) -> str:
        return f'{self.name} has {len(self.all_cards)}'
    
    def proceed_round_check(self, min_card_deal = 5):     
        if len(self.all_cards) < min_card_deal:
            print(f"\n{self.name} cannot deal current round of {min_card_deal} cards with only {len(self.all_cards)} cards left")  
            return False
        return True
    
    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def remove_cards(self, number_of_cards = 1):
        removed_cards = []
        self.round_count += 1

        for i in range(0, number_of_cards):
            removed_cards.append(self.remove_card())
        
        return removed_cards
    
    def player_cards_left_check(self):
        if len(self.all_cards) == 0: 
            print(f"Sorry, {self.name}, you have no cards left at round {self.round_count}!")
        else:
            print (f"{self.name} has {len(self.all_cards)} cards left at round {self.round_count}!")

    def declare_winner(self):
        print('\n')
        print("*" * 90)
        print(f"CONGRATULATION {self.name}, you won that game with {len(self.all_cards)} cards left at round {self.round_count}!")
        print("*" * 90)
        print('\n')

    def check_collateral_sufficiency(self, collateral):
        if len(self.all_cards) < collateral:
            print(f"Sorry, {self.name}, you have only {len(self.all_cards)} cards left, so you cannot collateralize {collateral} cards to declare a war")
            return False
        return True