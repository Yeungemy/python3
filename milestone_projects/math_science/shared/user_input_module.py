class UserInput:
    def whole_number(self):
        while True:
            try:
                user_input = int(input("Please enter a whole number: "));
                return user_input;
                break;
            except:
                print("That is not a whole number!");