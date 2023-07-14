import random
from IPython.display import clear_output

# promp user input a single character within required range
# @param {string[]} the list of characters
def player_marker_input(player_characters, message):
    letter = 'test' 

    while letter not in player_characters:
        user_input = input(f"{message} {player_characters}: " )

        if user_input.isalpha():
            letter = user_input[0].capitalize()
                
        if letter not in player_characters:
            print("Sorry, I cannot understand it. {} {}: ".format(message, player_characters))
            print('\n')

    return letter

def get_index_by_party_name(parties, first_acting_party):
    return parties.index(first_acting_party)

def display_curret_acting_party(parties, turn_count_no, pre_acting_party = '-'):
    current_turn = pre_acting_party

    if turn_count_no != 0: 
        index_turn_of_first_acting_party = get_index_by_party_name(parties, pre_acting_party)

        if index_turn_of_first_acting_party < len(parties) - 1:
            current_turn = parties[index_turn_of_first_acting_party + 1]
        else:
            current_turn = parties[index_turn_of_first_acting_party - 1]

        print('Current turn is party {}'.format(current_turn))
        print('\n')
    else:
        message ="Please choose which party go first"
        current_turn = player_marker_input(parties, message)

    return current_turn


def promp_for_a_digit(min_digit, max_digit, message):
    valid_digit = 0

    while valid_digit not in range(min_digit, max_digit):
        user_input = input("Please enter {} number (greater than or equal {} and less than {}): ".format(message, min_digit, max_digit))

        if user_input.isdigit():
            valid_digit = int(user_input)

    return valid_digit


def select_column():
    min_digit = 1
    max_digit = 4
    message = "column"
    temp_digit = promp_for_a_digit(min_digit, max_digit, message)

    if temp_digit == 1:
        position = 1
    elif temp_digit == 2:
        position = 3
    else:
        position = 5
                
    return position

def select_row():
    min_digit = 1
    max_digit = 4
    message = "row"
    temp_digit = promp_for_a_digit(min_digit, max_digit, message)

    if temp_digit == 1:
        position = 0
    elif temp_digit == 2:
        position = 1
    else:
        position = 2

    return position

def check_empty_new_state(game_board, cur_row_index, cur_col_index, position_original_value = '-'):
    return game_board[cur_row_index][cur_col_index] != position_original_value
    

def select_position():
    row_index = select_row()
    col_index = select_column()
    return [row_index, col_index]


def check_selected_position(game_board, position_original_value = '-'):
    overwritten = True

    while overwritten:
        current_position = select_position()
        overwritten = check_empty_new_state(game_board, current_position[0], current_position[1], position_original_value)

        if overwritten:
            print("Sorry, you are about to overwritten previous selection! please find another spot")
            print('\n')

    return current_position


def promp_for_confirmation(confirmation_answer_list, message):
    if player_marker_input(confirmation_answer_list, message) == 'Y':
        print('\n')
        print("We are starting a new adventure now. Good luck and have a fun!")
        print('\n')
        return True
    else:
        print('Bye-bye and see you next time')
        print('\n')
        return False

            
def place_marker(game_board, row_index, column_index, acting_part):
    game_board[row_index][column_index] = acting_part
    return game_board

def select_position_to_be_relocated(game_board, acting_party):
    is_correct_party = False

    while is_correct_party == False:
        # promp for a position to relocate
        cur_position = select_position()
        row_index = cur_position[0]
        col_index = cur_position[1]

        # get the value of selected position
        value_of_cur_position = game_board[row_index][col_index]

        # check the value of selected position match the acting party
        is_correct_party = (value_of_cur_position == acting_party)

        if is_correct_party == False:
            print("Sorry, that position is not your occupancy. Please choose one of yours!")
            print('\n')
    
    return cur_position


def switch_position(game_board, acting_party):
    original_value = '-'

    # display a warning of relocating an existing occupancy
    print('\n')
    print("WARNING!!! WARNING!!! Please carefully review existing occupancies and choose one of them to relocate!")
    print('\n')

    # promp for a position to be relocated
    cur_position = select_position_to_be_relocated(game_board, acting_party)

    # promp for a new position
    print("Please select a new empty position to place!")
    print('\n')
    new_position = check_selected_position(game_board)

    # take the new position
    game_board = place_marker(game_board, new_position[0], new_position[1], acting_party)

    # restore it to the original value
    game_board = place_marker(game_board, cur_position[0], cur_position[1], original_value)

    return game_board


def display_board(game_board):  
    print('\n')
    for i in range (0, len(game_board)):
        str = ''
        for j in range(0, len(game_board[i])):
            str += game_board[i][j]
        print(str)
    print('\n')
            

def same_element_array_check(game_board_row):
    is_same = True
    original_state_holder = '-'

    if original_state_holder in game_board_row:
        return False
    else:
        temp_item = game_board_row[len(game_board_row) - 1]
        for party in game_board_row:
            if is_same:
                is_same = (temp_item == party)

            else:
                return is_same
    return is_same
        
def row_match_check(game_board):
    win_state = False
    winner = '-'
    temp_row = []

    for test_row in game_board:
        if win_state == False:
            temp_row = [test_row[1], test_row[3], test_row[5]]      
            win_state = same_element_array_check(temp_row)
            winner = temp_row[0]
              
        else:
            return [True, winner]
        
    return [win_state, winner]
                   
def column_match_check(game_board):
    win_state = False
    test_row = ['', '', '']
    winner = '-'

    for col_index in [1, 3, 5]:
        if win_state == False:
            for row_index in [0, 1, 2]:
                test_row[row_index] = game_board[row_index][col_index]
            win_state = same_element_array_check(test_row)
            winner = test_row[0]

            if win_state:
                return [True, winner]
         
    return [win_state, winner]

def diagonals_match_check(game_board):
    cross_row_one = [game_board[0][1], game_board[1][3], game_board[2][5]]
    cross_row_two = [game_board[0][5], game_board[1][3], game_board[2][1]]
    
    # check cross row one
    win_state = same_element_array_check(cross_row_one) 
    winner = cross_row_one[0]   

    if win_state:
        return [win_state, winner]
    else:
        # check cross row two
        win_state = same_element_array_check(cross_row_two)
        winner = cross_row_two[0]
            
    return [win_state, winner]


def win_check(game_board):
    result = row_match_check(game_board)
    win_state = result[0]

    if win_state:
        return result
    else:
        result = column_match_check(game_board)
        win_state = result[0]

        if win_state:
            return result
        else: 
            result =diagonals_match_check(game_board)
            win_state = result[0]

            if win_state:
                return result       
    return result


def check_game_continue_state(game_board):
    result = win_check(game_board)
    win_state = result[0]
    winner_party = result[1]

    if win_state:
        print('\n')
        print("Congratulation, Party {}, You won that game!!!".format(winner_party))
        print('\n')
        return False
    else:
        return True
    
def replay():
    confirmation_answer_list = ['Y', 'y', 'N', 'n']
    message = 'Would like to play again: '
    
    return promp_for_confirmation(confirmation_answer_list, message)


def start_game_greeting():
    print('\n'* 100)
    print('Welcome to the tick tuck toe fun game!')


def game_on():
    want_play = True

    while want_play:
        game_board = [
            ['|', '-', '|', '-', '|', '-', '|'],
            ['|', '-', '|', '-', '|', '-', '|'],
            ['|', '-', '|', '-', '|', '-', '|']
        ]
        game_parties = ['X', 'O']
        turn_count = 0
        first_acting_party = '-'  
        continue_game = True

        # greeting to the tic tac toe game
        start_game_greeting()

        # print the game interface
        display_board(game_board)

        while continue_game:
            # display acting party
            acting_party = display_curret_acting_party(game_parties, turn_count, first_acting_party)
                
            if continue_game and turn_count < 6:
                # promp for a posion
                current_position = check_selected_position(game_board)

                # take the position for current part
                place_marker(game_board, current_position[0], current_position[1], acting_party)

            if continue_game and turn_count >= 6:
                # start relocate an existing role for each action from both part
                game_board = switch_position(game_board, acting_party)

            # print the game interface
            display_board(game_board)

            if turn_count >= 4:
                # detect game process
                continue_game = check_game_continue_state(game_board)

                if continue_game == False:
                    # send a request for playing again
                    want_play = replay()
         
            if continue_game:
                first_acting_party = acting_party
                turn_count += 1
                  

game_on()