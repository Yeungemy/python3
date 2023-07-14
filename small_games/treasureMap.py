# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
import random

man_len = len(map)
row_index = int(position[0])
col_index = int(position[1])

#validate the input
if row_index >= len(map):
  row_index = random.randint(0, man_len - 1)

if col_index >= len(map):
  col_index = random.randint(0, man_len - 1)

map[row_index][col_index] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")