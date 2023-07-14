# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = (input("What is your name? \n")).lower()
name2 = (input("What is their name? \n")).lower()
name_combine = name1 + name2
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
digits_true = name_combine.count('t') + name_combine.count('r') + name_combine.count('u') + name_combine.count('e')
digits_love = name_combine.count('l') + name_combine.count('o') + name_combine.count('v') + name_combine.count('e')
love_score = int(str(digits_true) + str(digits_true))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.") 
else:
  print(f"Your score is {love_score}.") 