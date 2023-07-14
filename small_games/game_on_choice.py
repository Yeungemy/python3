def display_game(game_list):
    print(game_list)

def gain_choice():
    gain_choice = 'wrong'

    while gain_choice not in [0, 1, 2]:
        # proper a gain choice
        gain_choice = int(input('Please enter a number (0, 1, 2): '))

    return gain_choice

def replace_choice(game_list, index):
    game_list[index] = input('Please enter a string to place at position: ')
    return game_list

def gain_on_choice() -> bool:
    gain_on_choice = ''

    while gain_on_choice not in ['Y', 'N']:
        gain_on_choice = input("Play again ('Y' = 'Yes', 'N' = 'No'): ")
        gain_on_choice = gain_on_choice.capitalize()

    if gain_on_choice == 'Y':
        return True
    else:
        return False

def game_on():
    game_on = True
    game_list = [0, 1, 2]

    while game_on == True:
        display_game(game_list)
        index = gain_choice()
        game_list = replace_choice(game_list, index)
        display_game(game_list)
        game_on = gain_on_choice()

    
    
game_on()