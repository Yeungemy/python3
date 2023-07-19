class Shared:
    def __init__(self, min_value = 0, max_value = 9999, msg = '', acceptable_list = []) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.msg = msg
        self.acceptable_list = acceptable_list

    def enter_digit(self):
        user_input = ' '

        while user_input not in range(self.min_value, self.max_value) or type(user_input) is not int:
            try:
                user_input = int(input(f"{self.msg}: "))
            except:
                print("Sorry, it is not an acceptable input and please try again!")
        return user_input
    
    def enter_character(self):
        user_input = ''

        while user_input not in self.acceptable_list:
            try:
                user_input = input(f"{self.msg}: ")

                if user_input.isalpha():
                    user_input = user_input.capitalize()
            except:
                print("Sorry, it is not an acceptable input and please try again!")
        return user_input