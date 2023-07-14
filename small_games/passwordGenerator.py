# list learning: append, sort, reverse have no return value
# pop (index): have return value

import random


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

new_password = []
random_index = 0
password_seeds = []

# get letters
for n in range(0, nr_letters):
    random_seed = random.choice(letters)
    password_seeds.append(random_seed)

# get symbols
for n in range(0, nr_symbols):
    random_seed = random.choice(symbols)
    password_seeds.append(random_seed)

# get numbers
for n in range(0, nr_numbers):
    random_seed = random.choice(numbers)
    password_seeds.append(random_seed)

print(f"the new password is " + ''.join(password_seeds))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password_seeds)
new_password =  "".join(password_seeds)

print("The most safety password is " + new_password)