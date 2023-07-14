class Shared:
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
    def request_confirmation(self, wish_message, bye_messgage):
        acceptable_answers = self.acceptable_answers
        message = "Please respond 'Yes' or 'No' ('{}'): ".format(acceptable_answers)
        user_input = self.user_input_characters(acceptable_answers, message)
        
        if user_input in self.positive_answers:
            print(wish_message)
            return True
        elif user_input in self.negative_answers:
            print(bye_messgage)
            return False
        else:
            print("Sorry, I don't understand it")

    # promp for user input a digit as required
    # @param {number[]} list of acceptable numbers
    def user_input_digit(self, acceptable_digit):
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