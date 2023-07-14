import random
deck = ["rock", "paper", "scissors"]
start_game = 'y'

while start_game == 'y':
    start_game = (input("Game over. Play again, 'Y' or 'y' for yes or others for no?\n")).lower()

    if start_game == 'y':
        print('\n************************')
        print('     starting Game!')
        print('************************\n')

        user_shoot_index = int(input("What are going to shoot this run, 0 fro rock, 1 for paper, or 2 for scissors?\n\n"))
        
        computer_shoot_index = random.randint(0, 2)
        computer_shoot = deck[computer_shoot_index]
        
        if user_shoot_index < 0 or user_shoot_index > 2:
            print("invalid number. You lose!")
        elif user_shoot_index == computer_shoot_index:
            print("You won a draw.")
        elif user_shoot_index > computer_shoot_index:
            if user_shoot_index == 2 and computer_shoot_index == 0:
                print("You lose")
            else:
                print("You won.")
        elif user_shoot_index < computer_shoot_index:
            if user_shoot_index == 0 and computer_shoot_index == 2:
                print("You won.")
            else:
                print("You lose")

        print('************************')
        print(f"{deck[user_shoot_index]} VS {computer_shoot}")
        print('************************\n')
            
    else:
        print('Good bye and see you next time!')   