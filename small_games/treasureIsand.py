print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

decision_made = (input("Left or right?\n")).lower()
if decision_made == 'left':
  decision_made = (input("Swim or Wait?\n")).lower()
  if decision_made == 'wait':
    decision_made = (input("which door, red, blue, or yellow?\n")).lower()
    if decision_made == 'yellow':
      print("You won")
    else:
      print("Game Over")
  else:
    print("Game Over")
  
else:
  print("Game Over")