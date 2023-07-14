from random import shuffle

my_list = [' ', ' ', 'O', ' ', ' ']

# shuffle
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list 

# proper a guess
def play_guess():
    number_guess = 1000 

    while number_guess not in [0, 1, 2, 3, 4]:
        number_guess = int(input('Pick a number from [0, 1, 2, 3, 4]: '))
    
    return number_guess

# check guess
def check_guess(guess_number, my_list):
    result = ''

    if my_list[guess_number] == 'O':
        result = 'You are won'
    else:
        result = 'Wrong guess and try again'
    return result

def start_game(my_list):
    guess_number = 0
    game_result = ''

    # shuffle
    shuffle_list(my_list)

    # play guess
    guess_number = play_guess()

    # check guess
    game_result = check_guess(guess_number, my_list)

    print(game_result)
    print(my_list)


start_game(my_list)



