from cardModule import Card
from deckModule import Deck
from chipsModule import Chips
from handModule import Hand

game_on = True
player_chips = Chips()

while game_on:
    take_round = True

    while take_round:
        # define player hands
        player_hand = Hand('Player')
        dealer_hand = Hand('Dealer')
        
        # creat 52 cards
        test_deck = Deck()

        # shuffle the deck
        test_deck.shuffle()

        # display greeting
        test_deck.greeting()

        # request for a bet
        player_chips.make_bet()

        # deal two card to both the player and the dealer
        test_deck.deal_first_two_cards(player_hand, dealer_hand)

        # request for hit or stand from player
        player_hand.hits(test_deck)

        # request for hit or stand from dealer
        dealer_hand.hits(test_deck, True)

        # win check
        test_deck.win_check(player_hand, dealer_hand, player_chips)

        # request a replay
        take_round = False
        game_on = test_deck.replay_check()

        if not game_on:
            # print summary for player
            player_chips.calculate_earnings()
