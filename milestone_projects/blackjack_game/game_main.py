from deck import Deck
from player import Player
from war import War
from random import shuffle
from share_module import Shared
from chip import Chip

game_on = True
msg = 'to start Blackjack game?'
replayMsg = 'to replay Blackjack game?'
hitOrStopMsg = 'to hit for one more card?'
min = 100
max = 150
minBetMoney = 5

newChip = Chip(min)
shared = Shared()

while game_on:
    dealerHit = True
    playerHit = True
    take_round = True
    round_count = 0
    dealerFirstRoundPoints = 0
    moneyDepositRequestMsg = 'of total money to deposit for games'
    moneyBetMsg = "of bet money for the current round"
    depositIncreaseMsg = "to increase chip money: "
    war = War()
    
    # create player
    player = Player('Player A')

    # create another player as dealer
    dealer = Player('Dealer')

    # define a new deck and shuffle it
    new_deck = Deck()
    new_deck.shuffle()

    # greet to players
    war.displayGreetingMsg()

    if newChip.total < minBetMoney:
        print(f"{player.name} only has ${newChip.total} left!")
        
        if shared.request_confirmation(depositIncreaseMsg):
            newChip.total += shared.inputDigitWithinRange(min, max, moneyDepositRequestMsg)
        else:
            take_round = False
            game_on = False
            print('Bye-bye')
    else:
        # request a bet for current round
        newChip.bet = shared.inputDigitWithinRange(minBetMoney, newChip.total, moneyBetMsg)
        

    while take_round:
        # check player points, if above 21, dealer declare as winner immediately 
        if player.points > 21:
            take_round = False

            # dealer declare as winner without any disclosure
            print(f"\n\nI, {dealer.name}, won that game since {player.name} has above 21 points")

            # lose bet and money out
            newChip.loseBet()

        elif not playerHit and not dealerHit:
            take_round = False

            # desclosure final points of the dealer
            print(f'{dealer.name} has the total of {dealer.points} points')

            # check whether dealer's points is above 21
            if dealer.points > 21:
                print(f'\n\nI, {player.name} with  total {player.points} points, won that game')

                # won game and money deposit
                newChip.winBet()
            elif dealer.points > player.points:
                print(f'\n\nI, {dealer.name} with  total {dealer.points} points, won that game')

                # lose bet and money out
                newChip.loseBet()

            elif dealer.points < player.points:
                print(f'\n\nI, {player.name} with  total {player.points} points, won that game')

                # won game and money deposit
                newChip.winBet()
            else:
                print("TIE GAME")

        if not take_round:
            game_on = war.requestStartGameNow(replayMsg)
        else:
            if playerHit:
                playerHit = war.requestStartGameNow(hitOrStopMsg)

                if playerHit:
                    player_new_card = new_deck.deal_one()
                    print(player_new_card)

                    player.addPoints(player_new_card) 

                    if player_new_card.rank == 'Ace':
                        print(f"Very lucky, {player.name} has got {player.aces} Aces")

            '''
            if it is first round, dealer take the first card and show the face value
            otherwise, dealer secret calculate the card and sciently decide to hit or stop after each action from player
            '''

            # dealer dcide to follow the player's each hit
            if dealerHit and dealer.points < 17:
                dealer_new_card = new_deck.deal_one()
                dealer.addPoints(dealer_new_card)

                if round_count == 0: 
                    dealerFirstRoundPoints = dealer_new_card.face_value
                
            else:
                dealerHit = False
            
            # display the dealer's points for the first card
            print(f"Dealer's points from the first round is {dealerFirstRoundPoints} points")

            # display player current points
            print(f'The player so far has {player.points} points!') 

        round_count += 1
            
