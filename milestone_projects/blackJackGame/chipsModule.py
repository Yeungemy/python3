'''
This class hold chips of the players
'''

from sharedModule import Shared
shared = Shared()

class Chips:
    def __init__(self, total = 100) -> None:
        self.total = total
        self.bet = 5
        self.loss = 0
        self.win = 0

    def __str__(self) -> str:
        return f"The balance of chips are {self.total}"

    def make_bet(self, min = 5):
        if self.total < min or self.total < self.bet:
            print("\n" * 3) 
            print("*******************************************************************************\n")
            if self.total < min:
                print(f"WARNING! You, only {self.total} chips at hand, cannot support the minimum bet of {min}!")
            else:
                print(f"WARNING! You, only {self.total} chips at hand, cannot support the bet of {self.bet}!")
            print("\n*******************************************************************************\n")

            self.add_chips()

        shared.min_value = min
        shared.max_value = self.total
        shared.msg = f'Please make a bet between {min} and {self.total}'

        self.bet = shared.enter_digit()
        print(f"\nCurrent bet is {self.bet} chips. \nBefore starting, please kindly be reminded that 'Aces' can be value 1 of 11 if needed. \nStart now and good luck!")

    def add_chips(self, min = 5, max = 999):
        shared.max_value = min
        shared.max_value = max
        shared.msg = f'Please add chips betwee {min} and {max}'

        self.total += shared.enter_digit()

    def win_bet(self):
        self.total += self.bet
        self.win += self.bet 

    def lose_bet(self):
        self.total -= self.bet
        self.loss += self.bet
    
    def calculate_earnings(self):
        earnings = self.win - self.loss

        print("\n" * 3) 
        print("*******************************************************************************\n")
        if earnings > 0:
            print(f"Congratulation, you have earned ${earnings}!!!")
        elif earnings < 0:
            print(f"Sorry, you have lost ${-earnings} and good luck next time")
        else:
            print("You have lots of fun here without earning or loss any money at all!")

        print("\n*******************************************************************************\n")