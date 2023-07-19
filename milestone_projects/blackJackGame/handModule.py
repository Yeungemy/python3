'''
This class hold player class
'''

from sharedModule import Shared
shared = Shared()


class Hand:
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        self.values = 0
        self.aces = 0

    def __str__(self) -> str:
        print(f"\n{self.name}'s cards: ")
        cardComp = ''
        for card in self.cards:
            cardComp += card.__str__() + '\n'

    def add_one(self, card):
        self.cards.append(card)
        self.values += card.faceValue

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_aces(self):
        while self.values > 21 and self.aces:
            self.aces -= 1
            self.values -= 10

    # print all cards
    def display_all_cards(self):
        print(f"\n{self.name}'s cards: ")
        print(*self.cards, sep = '\n')
    
    # print all cards except the first one
    def display_some_cards(self):
        print(f"\n{self.name}'s cards: ")
        for card in self.cards[1:]:
            print(card)

    def hit_check(self):
        shared.acceptable_list = ['S', 'H']
        shared.msg = f"\nPlease tell stand or hit ('S' or 's' for 'stand', and 'H' OR 'h' for hit): "
        answer = shared.enter_character()

        if answer == 'H':
            return True
        else:
            return False
        
    def hits(self, test_deck, is_dealer = False):
        if is_dealer:
            self.adjust_aces()

            while self.values < 17:
                new_card = test_deck.deal_one()
                self.add_one(new_card)
                self.adjust_aces()
                self.display_some_cards()
        else:
            is_busted = False

            while not is_busted:
                self.adjust_aces()
                is_busted = self.values > 21

                if is_busted:
                    print(f"{self.name} is busted")
                else:
                    answer = self.hit_check()
                    if answer:
                        new_card = test_deck.deal_one()
                        self.add_one(new_card)
                        self.display_all_cards()
                    else: 
                        break

            self.adjust_aces()

            
            

    
