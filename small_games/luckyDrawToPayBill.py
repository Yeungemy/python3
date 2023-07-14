# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

random_index = random.randint(0, len(names) - 1)
lucky_payer = names[random_index]
print(random_index)
print(names)
print(names[random_index])

print(f"{lucky_payer} will be apprciated for have all of us for a dinner")