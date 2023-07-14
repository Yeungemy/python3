from card import Card
from player import Player
from deck import Deck
from random import shuffle
from share_module import Shared
from random import randint

'''
Game logic
1. create two players
2. create 52 cards
3. shuffle all cards
4. split all cards evenly to two players
5. start game round
    5.1. count cards on each player to check a potential winner now
        5.1.1 check potential winner
            5.1.1.1. if one of player has no cards on hand, he lose 
        5.1.2. stop the round
        5.1.3. declare the game result, and
        5.1.4. request replay
    5.2  each player draw a card
    5.2. compare face values of the cards
    5.3. winner collect two cards, if a war occurs, and then
        5.3.1. ask each player to show number of cards on hands 
        5.3.2. promp for each player to draw random number of cards out of their hands
        5.3.3. compare the number to be drawn and the number of cards on each player's hand, if unsufficient carts left of any player, then declare war end and winner
        5.3.4. draw all cards out from each player, 
        5.3.5. repeat step 5 and its substeps underneath
'''
game_on = True
shared = Shared()

while game_on:
    number_of_max_cards_removed = 14
    round_count = 0
    take_round = True

    # define players
    player_one = Player('Jacie')
    player_two = Player('Alice')

    # define a new deck
    new_deck = Deck()

    # set all cards
    all_cards = new_deck.all_cards
    
    # shuffle all cards
    new_deck.shuffle()

    # split cards into two decks
    new_deck.split_cards_by_players(player_one, player_two)
    player_one_cards = player_one.all_cards
    player_two_cards = player_two.all_cards

    # start a round
    while take_round:
        round_count += 1

        # identify potential winner
        if len(player_one_cards) == 0 and len(player_two_cards) == 0:
            print("That is a tie game since both parties have no cards on the hand")

            # stop the round
            take_round = False

            # request for a replay
            game_on = shared.request_confirmation('Start again and have fun!', 'Bye-bye!')
        elif len(player_one_cards) == 0:
            # declare a winner is player two
            print(f"Here is round {round_count}! {player_one.name} has no cards on hand")
            print(f"Here is round {round_count}! {player_two.name} has {len(player_two.all_cards)}")
            print(f"Congratulation {player_two.name}, you won that game at round {round_count}!")

            # stop the round
            take_round = False

            # request for a replay
            game_on = shared.request_confirmation('Start again and have fun!', 'Bye-bye!')
        elif len(player_two_cards) == 0:
            # declare a winner is player two
            print(f"Here is round {round_count}! {player_two.name} has no cards on hand")
            print(f"Here is round {round_count}! {player_one.name} has {len(player_one.all_cards)}")
            print(f"Congratulation {player_one.name}, you won that game at round {round_count}!")

            # stop the round
            take_round = False

            # request for a replay
            game_on = shared.request_confirmation('Start again and have fun!', 'Bye-bye!')

        else:
            # draw a card
            card_one = player_one.remove_card()
            card_two = player_two.remove_card()

            # compare and declare a winner or a war
            if card_one.face_value > card_two.face_value:

                # player one collect cards
                player_one.add_cards([card_one, card_two])

            elif card_one.face_value < card_two.face_value:
                player_two.add_cards([card_one, card_two])

            else:
                # display number of cards to be required for a war
                number_of_cards_for_war = randint(5, number_of_max_cards_removed)

                print(f'WAR ALERT!!! That is a war at round {round_count}! {number_of_cards_for_war} cards are required to declare a war')

                # check number of cards remaining on each player's hands
                if len(player_one_cards) < number_of_cards_for_war and len(player_two_cards) < number_of_cards_for_war:
                    print("That is a tie game since both parties have no enought cards to declare a war")

                    # stop the round
                    take_round = False

                    # request for a replay
                    game_on = shared.request_confirmation('Start again and have fun!', 'Bye-bye!')
                elif len(player_one.all_cards) < number_of_cards_for_war:

                    # declare a winner is player two
                    print(f"Sorry, {player_one.name}, you only have {len(player_one.all_cards)} left, so you cannot declare a war")
                    print(f"Congratulation {player_two.name}, you won that gain at round {round_count} with {len(player_two.add_cards - number_of_cards_for_war)} cards!")

                    # stop the round
                    take_round = False

                    # request for a replay
                    game_on = shared.request_confirmation('Start again and have fun!', 'Bye-bye!')
                    
                elif len(player_two.all_cards) < number_of_cards_for_war:

                    # declare a winner is player two
                    print(f"Sorry, {player_two.name}, you only have {len(player_two.all_cards)} left, so you cannot declare a war")
                    print(f"Congratulation {player_one.name}, you won that gain at round {round_count} with {len(player_two.add_cards - number_of_cards_for_war)} cards!")

                    # stop the round
                    take_round = False

                    # request for a replay
                    game_on = shared.request_confirmation('Start again and have fun!', 'Bye-bye!')
                else:
                    # player one remove cards for the war
                    player_one.remove_cards(number_of_cards_for_war)

                    # player two remove cards for the war
                    player_two.remove_cards(number_of_cards_for_war)
