from player_module import Player
from deck_module import Deck
from wars_module import Wars
from share_module import Shared

game_on = True
shared = Shared()
msg = 'to replay the game'
max_deal = 10
min_deal = 1

player_one = Player('Player_A', 0)
player_two = Player('Player_b', 0)


while game_on:
    take_round = True
    round_count = 0

    # define a new deck
    new_deck = Deck()

    # define a war
    wars = Wars(0)

    # set all cards
    all_cards = new_deck.all_cards
    
    # shuffle all cards
    new_deck.shuffle()

    # split cards into two decks
    new_deck.split_cards_by_players(player_one, player_two)

    # start a round
    while take_round:
        round_deal = shared.get_randon_integer(min_deal, max_deal)
        player_one_proceed_around = player_one.proceed_round_check(round_deal)
        player_two_proceed_around = player_two.proceed_round_check(round_deal)
        take_round = player_one_proceed_around and player_two_proceed_around
        
        # check whether both player have the capability to take round
        if not take_round:
            player_one.player_cards_left_check()
            player_two.player_cards_left_check()
            
            # summary war cost
            wars.wars_collateral_update()

            if not player_one_proceed_around and not player_two_proceed_around:
                # declare a tie game
                wars.declare_tie_game()
            elif not player_one_proceed_around:
                # player two declare as winner
                player_two.declare_winner()
            else:
                # player one declare as winner
                player_one.declare_winner()
            
            game_on = shared.request_confirmation(msg)

        else:
            # identify potential winner
            player_one.round_count += 1
            player_two.round_count += 1
            player_one_turn_deal_cards = []
            player_two_turn_deal_cards = []

            # proceed a round
            player_one_turn_deal_cards.extend(player_one.remove_cards(round_deal))
            player_two_turn_deal_cards.extend(player_two.remove_cards(round_deal))

            # compare and declare a winner or a war
            if player_one_turn_deal_cards[-1].face_value > player_two_turn_deal_cards[-1].face_value:
                # player one collect cards
                player_one.add_cards(player_one_turn_deal_cards)
                player_one.add_cards(player_two_turn_deal_cards)

            elif player_one_turn_deal_cards[-1].face_value < player_two_turn_deal_cards[-1].face_value:
                # player one collect cards
                player_two.add_cards(player_one_turn_deal_cards)
                player_two.add_cards(player_two_turn_deal_cards)

            else:
                wars.war_collateral = shared.get_randon_integer(min_deal, max_deal)
                
                # alert a war
                wars.war_alert()

                # check the probability in war
                player_one_declaring_war = player_one.check_collateral_sufficiency(wars.war_collateral)
                player_two_declaring_war = player_two.check_collateral_sufficiency(wars.war_collateral)
                probability_in_war = player_one_declaring_war and player_two_declaring_war

                if probability_in_war:
                    # deal collateral
                    player_one.remove_cards(wars.war_collateral)
                    player_two.remove_cards(wars.war_collateral)
                else:
                    take_round = False
                    player_one.player_cards_left_check()
                    player_two.player_cards_left_check()
                    
                    # summary war cost
                    wars.wars_collateral_update()
                    print(f"Each player have dealt {round_deal} cards for the last round")

                    if not player_one_declaring_war and not player_two_declaring_war:
                        wars.declare_tie_game()
                    elif player_one_declaring_war:
                        player_one.declare_winner()
                    elif player_two_declaring_war:
                        player_two.declare_winner() 

                    # request for a replay
                    game_on = shared.request_confirmation(msg)                     
            