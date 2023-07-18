from deck import Deck
from player import Player
from war import War
from random import shuffle
from share_module import Shared

game_on = True
msg = 'to start Blackjack game?'
replayMsg = 'to replay Blackjack game?'
hitOrStopMsg = 'to hit for one more card?'

while game_on:
    dealerHit = True
    playerHit = True
    take_round = True
    round_count = 0
    dealerFirstRoundPoints = 0
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

    while take_round:
        # check player points, if above 21, dealer declare as winner immediately 
        if player.points > 21:
            take_round = False

            # dealer declare as winner without any disclosure
            print(f"\n\nI, {dealer.name}, won that game since {player.name} has above 21 points")

        elif not playerHit and not dealerHit:
            take_round = False

            # desclosure final points of the dealer
            print(f'{dealer.name} has the total of {dealer.points} points')

            # check whether dealer's points is above 21
            if dealer.points > 21:
                print(f'\n\nI, {player.name} with  total {player.points} points, won that game')
            elif dealer.points > player.points:
                print(f'\n\nI, {dealer.name} with  total {dealer.points} points, won that game')
            elif dealer.points < player.points:
                print(f'\n\nI, {player.name} with  total {player.points} points, won that game')
            else:
                print("TIE GAME")

        if not take_round:
            game_on = war.requestStartGameNow(replayMsg)
        else:
            if playerHit:
                playerHit = war.requestStartGameNow(hitOrStopMsg)

                if playerHit:
                    player_new_card = new_deck.deal_one()
                    player.points += player_new_card.face_value 

            '''
            if it is first round, dealer take the first card and show the face value
            otherwise, dealer secret calculate the card and sciently decide to hit or stop after each action from player
            '''

            # dealer dcide to follow the player's each hit
            if dealerHit and dealer.points < 17:
                dealer_new_card = new_deck.deal_one()
                dealer.points += dealer_new_card.face_value

                if round_count == 0: 
                    dealerFirstRoundPoints = dealer_new_card.face_value
                
            else:
                dealerHit = False
            
            # display the dealer's points for the first card
            print(f"Dealer's points from the first round is {dealerFirstRoundPoints} points")

            # display player current points
            print(f'The player so far has {player.points} points!') 

        round_count += 1
            
