from random import randint

class Shared:
    wish_msg = ''
    bye_msg = ''

    def __init__(self) -> None:
        self.acceptable_answers = ['Yes', 'yes', 'YES', 'Y', 'y', 'No', 'no', 'NO', 'n', 'N']
        self.positive_answers = ['Yes', 'yes', 'YES', 'Y', 'y']
        self.negative_answers = ['No', 'no', 'NO', 'n', 'N']

    # promp for user input a character as required
    # @param {string[]} list of acceptable characters
    # @param {string} message - the message to remender user to enter as required
    def user_input_characters(self, acceptable_characters, message):
        user_input = ''

        while not user_input.isalpha() or user_input not in acceptable_characters:
            user_input = input(message).upper()

            if not user_input.isalpha() or user_input not in acceptable_characters:
                print(message)

        return user_input

    # request a answer 'Yes' or 'No'
    # param {string[]} acceptable_answers - the qualified list of answers to be input
    def request_confirmation(self, msg):
        acceptable_answers = self.acceptable_answers
        message = "\nPlease respond 'y' = 'Yes' or 'n' = 'No' {}: ".format(msg)
        user_input = self.user_input_characters(acceptable_answers, message)
        
        if user_input in self.positive_answers:
            print(self.wish_msg)
            return True
        elif user_input in self.negative_answers:
            print(self.bye_msg)
            return False
        else:
            print("Sorry, I don't understand it")

    # promp for user input a digit as required
    # @param {number[]} list of acceptable numbers
    def user_input_digit(self, acceptable_digit, msg = ''):
        digit_input = 0

        # always check the digit input is in acceptable range
        while digit_input not in acceptable_digit:
            # promp for a digit 
            user_input = input("Please enter a digit {}: ".format(msg))

            # check whether the user input is a digit
            if user_input.isnumeric():
                # convert the user input to a integer if it is a digit
                digit_input = int(user_input)

                # send a reminder if the user input is not a digit
                if digit_input not in acceptable_digit:
                    print("That digit is out of the acceptable list: ")

        return digit_input
    
    # promp for user input a digit as required
    # @param {number[]} list of acceptable numbers
    def inputDigitWithinRange(self, min, max, msg = ''):
        digit_input = min - 1

        # always check the digit input is in acceptable range
        while digit_input not in range(min, max):
            # promp for a digit 
            user_input = input("Please enter a digit {} within ({}, {}): ".format(msg, min, max))

            # check whether the user input is a digit
            if user_input.isnumeric():
                # convert the user input to a integer if it is a digit
                digit_input = int(user_input)

                # send a reminder if the user input is not a digit
                if digit_input not in range(min, max):
                    print("That digit is out of the acceptable list: ")

        return digit_input
    
    def get_randon_integer(self, min, max):
        return randint(min, max)
    
    # promp for user input a character as required
    # @param {string[]} list of acceptable space characters
    # @param {string} message - the message to remender user to enter as required
    def user_input_characters(self, acceptable_characters, message):
        user_input = ''

        while not user_input.isalpha() or user_input not in acceptable_characters:
            user_input = input(message).upper()

            if not user_input.isalpha() or user_input not in acceptable_characters:
                print(message)

        return user_input


    # player choose space marker
    # @param {string[]} list of acceptable space characters
    def choose_player_marker(self, acceptable_characters):
        player2 = acceptable_characters[0]
        message = "Please enter a single alphabet ('{}' or '{}'): ".format(acceptable_characters[0], acceptable_characters[1])
        player1 = self.user_input_characters(acceptable_characters, message)
        index_of_player1 = acceptable_characters.index(player1)

        if index_of_player1 == 0:
            player2 = acceptable_characters[1]    

        return (player1, player2)

    def display_player_marker(self, player_marker):
        print("Current player is about to place a marker '{}' on the game board".format(player_marker))
