'''
This class hold 52 cards
'''
from cardModule import Card
from random import shuffle
from sharedModule import Shared

shared = Shared()

suits = ('Spades♤', 'Hearts♡', 'Diamonds◇', 'Clubs♧')
ranks = (
    'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
    'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack'
    )

class Deck:
    def __init__(self) -> None:
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self) -> str:
        cardComp = ''
        for card in self.deck:
            cardComp += card.__str__() + '\n'
        return cardComp
    
    def greeting(self):
        print("\n" * 100)
        print("Welcome BlackJack Game Board!\n")
    
    def shuffle(self):
        shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()
    
    def replay_check(self):
        shared.acceptable_list = ['Y', 'N']
        shared.msg = f"\n\nWould you like replay the game ('Y', or 'y' for 'Yes', 'N', 'n' for 'No')"
        answer = shared.enter_character()

        if answer == 'Y':
            return True
        else:
            return False
        
    def deal_first_two_cards(self, player_hand, dealer_hand):
        # deal two card to both the player and the dealer
        for i in range (0, 2):
            for hand in (player_hand, dealer_hand):
                new_card = self.deal_one()
                hand.add_one(new_card)

        player_hand.display_all_cards()
        dealer_hand.display_some_cards()

    def win_check(self, player_hand, dealer_hand, player_chips):
        print("\n" * 3) 
        print("************************************************************************\n")
    
        if player_hand.values > 21:
            print(f"Sorry {player_hand.name}, you busted and lost the bet!")
            player_chips.lose_bet()
            print("\n************************************************************************")
        else:
            if dealer_hand.values > 21:
                print(f"{dealer_hand.name} busted. \n\nCONGRATULATION {player_hand.name}, you won the bet!")
                player_chips.win_bet()
            elif dealer_hand.values < player_hand.values:
                print(f"CONGRATULATION {player_hand.name}, you won the bet with more points than the dealer!")
                player_chips.win_bet()
            else:
                print(f"Sorry {player_hand.name}, you lost the bet with less points than the dealer!")
                player_chips.lose_bet()
            
            print("\n************************************************************************")

            player_hand.display_all_cards()

            # dealer display all hards
            dealer_hand.display_all_cards()
