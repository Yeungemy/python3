# greeting to the player with warn welcome to the game board
def welcome_to_game_board():
    print("Welcome to the tic tac toe game board")


# display updated game board
def display_game_board(game_board):
    row_one = '|' + game_board[1] + '|' + game_board[2] + '|' + game_board[3] + '|'
    row_two = '|' + game_board[4] + '|' + game_board[5] + '|' + game_board[6] + '|'
    row_three = '|' + game_board[7] + '|' + game_board[8] + '|' + game_board[9] + '|'

    print(row_one)
    print(row_two)
    print(row_three)


# request a confirmation as required
# param {string[]} acceptable_answers - the qualified list of answers to be input from players
def request_confirmation(acceptable_answers, wish_message, bye_messgage):
    message = "Please confirm to start a new game ('{}'): ".format(acceptable_answers)
    user_input = user_input_characters(acceptable_answers, message)
    positive_answers = ['Yes', 'yes', 'YES', 'Y', 'y']
    negative_answers = ['No', 'no', 'NO', 'n', 'N']

    if user_input in positive_answers:
        print(wish_message)
        return True
    elif user_input in negative_answers:
        print(bye_messgage)
        return False
    else:
        print("Sorry, I don't understand it")
    

# check start game status
# param {string[]} acceptable_answers - the qualified list of answers to be input from players
def start_game_check(acceptable_answers):
    wish_msg = "Start now! Good luck!"
    bye_msg = "See you next time!"

    return request_confirmation(acceptable_answers, wish_msg, bye_msg)
    

# check start game status
# param {string[]} acceptable_answers - the qualified list of answers to be input from players
def replay_check(acceptable_answers):
    wish_msg = "Would you like to play again!"
    bye_msg = "See you next time!"

    return request_confirmation(acceptable_answers, wish_msg, bye_msg)


# promp for user input a character as required
# @param {string[]} list of acceptable space characters
# @param {string} message - the message to remender user to enter as required
def user_input_characters(acceptable_characters, message):
    user_input = ''

    while not user_input.isalpha() or user_input not in acceptable_characters:
        user_input = input(message).upper()

        if not user_input.isalpha() or user_input not in acceptable_characters:
            print(message)

    return user_input


# player choose space marker
# @param {string[]} list of acceptable space characters
def choose_player_marker(acceptable_characters):
    player2 = acceptable_characters[0]
    message = "Please enter a single alphabet ('{}' or '{}'): ".format(acceptable_characters[0], acceptable_characters[1])
    player1 = user_input_characters(acceptable_characters, message)
    index_of_player1 = acceptable_characters.index(player1)

    if index_of_player1 == 0:
        player2 = acceptable_characters[1]    

    return (player1, player2)

def display_player_marker(player_marker):
    print("Current player is about to place a marker '{}' on the game board".format(player_marker))


# promp for user input a digit as required
# @param {number[]} list of acceptable space numbers
def user_input_digit(acceptable_digit):
    position = 0

    # always check the digit input is in acceptable range
    while position not in acceptable_digit:
        # promp for a digit 
        user_input = input("Please enter a digit {}: ".format(list(acceptable_digit)))

        # check whether the user input is a digit
        if user_input.isdigit():
            # convert the user input to a integer if it is a digit
            position = int(user_input)

            # send a reminder if the user input is not a digit
            if position not in acceptable_digit:
                print("That digit is out of the acceptable list {}: ".format(list(acceptable_digit)))

    return position


# player mark space on the game board
# @param {string[]} game_board - the game board 
# @param {number[]} acceptable_digit - the list of digit 
# @param {string} player_marker - the player's space marker
def place_marker(game_board, acceptable_digit, player_marker):
    # promp for a position to place marker on the game board
    position = user_input_digit(acceptable_digit)

    # place marker on the game board as required
    game_board[position] = player_marker

    return game_board

# request to play again
def replay_request(acceptable_answers):
    wish_message = "Would you like to play again?"
    bye_message = "Bye and see you next time"

    return request_confirmation(acceptable_answers, wish_message, bye_message)


# check whether the game board is out of space
def full_game_board_check(game_board, space_placeholder = '-'):
    return space_placeholder not in game_board

# check whether players are in tie game situation or not
def tie_game_check(game_board, space_placeholder = '-'):
    if full_game_board_check(game_board, space_placeholder):
        print("It is a tie game!")
        return True
    else: 
        return False


# check whether items in row/co/diagnoals match each other
def match_check(game_board_row, acting_player_marker, space_placeholder = '-'):
    if space_placeholder not in game_board_row and acting_player_marker in game_board_row:
        return game_board_row[0] == game_board_row[1] and game_board_row[1] == game_board_row[2]
    else:
        return False
        

# check whether items in each row match each other ot not
def row_match_check(game_board, acting_player_marker, space_placeholder = '-'):
    test_row_one = [game_board[1], game_board[2], game_board[3]]
    test_row_two = [game_board[4], game_board[5], game_board[6]]
    test_row_three = [game_board[7], game_board[8], game_board[9]]

    win_state = match_check(test_row_one, acting_player_marker, space_placeholder) 

    if win_state:
        return win_state
    else:
        win_state = match_check(test_row_two, acting_player_marker, space_placeholder)

        if win_state:
            return win_state
        else:
            win_state = match_check(test_row_three, acting_player_marker, space_placeholder)

    return win_state
    

# check whether items in each column match each other ot not 
def col_match_check(game_board, acting_player_marker, space_placeholder = '-'):
    test_col_one = [game_board[1], game_board[4], game_board[7]]
    test_col_two = [game_board[2], game_board[5], game_board[8]]
    test_col_three = [game_board[3], game_board[6], game_board[9]]

    win_state = match_check(test_col_one, acting_player_marker, space_placeholder) 

    if win_state:
        return win_state
    else:
        win_state = match_check(test_col_two, acting_player_marker, space_placeholder)

        if win_state:
            return win_state
        else:
            win_state = match_check(test_col_three, acting_player_marker, space_placeholder)

    return win_state


# check whether items in each diagonal match each other ot not
def diagonals_match_check(game_board, acting_player_marker, space_placeholder = '-'):
    test_diagonals_one = [game_board[1], game_board[5], game_board[9]]
    test_diagonals_two = [game_board[7], game_board[5], game_board[3]]

    win_state = match_check(test_diagonals_one, acting_player_marker, space_placeholder) 

    if win_state:
        return win_state
    else:
        win_state = match_check(test_diagonals_two, acting_player_marker, space_placeholder)

    return win_state


# winner check
def win_check(game_board, acting_player_marker, space_placeholder = '-'):
    win_state = row_match_check(game_board, acting_player_marker, space_placeholder)
        
    if win_state:
        return win_state
    else:
        win_state = col_match_check(game_board, acting_player_marker, space_placeholder)

        if win_state:
            return win_state
        else:
            win_state = diagonals_match_check(game_board, acting_player_marker, space_placeholder)
        
    return win_state


# progress report
def progress_report(game_board, acting_player_marker, acceptable_answers, space_placeholder = '-'):
    # check win state
    win_state = win_check(game_board, acting_player_marker, space_placeholder)

    if win_state:
        # if there is a winner, a congratulation message is displaying
        print("Congratulation, player with marker {} won that game!".format(acting_player_marker))

    else:
        # check whether it is involved in a tie game situation
        win_state = tie_game_check(game_board, space_placeholder)
    
    return win_state


# tic tac toe game 
def tic_tac_toe_game():
    start_game = True

    while start_game: 
        game_board = ['$', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        acceptable_characters = ['X', 'O']
        player_turn = ['', '']
        acceptable_digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        acceptable_answers = ['Yes', 'yes', 'YES', 'Y', 'y', 'No', 'no', 'NO', 'n', 'N']
        turn_count = 0
        space_placeholder = '-'
        

        # greeting to the players
        welcome_to_game_board()

        # request to start the game
        continue_game = start_game_check(acceptable_answers)

        if not continue_game:
            start_game = False
        else:
            # display the game board
            display_game_board(game_board)

            # request player to choose their space marker
            player_turn[0], player_turn[1] = choose_player_marker(acceptable_characters)

            while continue_game:
                # define acting player
                current_player_marker = player_turn[turn_count % 2]

                # display the first acting player
                display_player_marker(current_player_marker)

                # the first player places the marker
                place_marker(game_board, acceptable_digit, current_player_marker)

                # display the game board
                display_game_board(game_board)

                # check game status
                if turn_count >= 4:
                    win_state = progress_report(game_board, current_player_marker, acceptable_answers, space_placeholder)

                    if win_state:
                        continue_game = False
                        start_game = replay_check(acceptable_answers)
                else:
                    # count turns
                    turn_count += 1

    
# trigger the game board
tic_tac_toe_game()
