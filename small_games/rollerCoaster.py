height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    age = int(input("How old ar you? "))
    if age < 12:
        bill += 5
    elif age < 45 or age > 55:
        bill += 7
        
    photo_wanted = input("Want photos? ")
    if photo_wanted == 'Y':
        bill += 3
        
    print(f"The total bill is ${bill}")
        
else:
    print("You cannot ride.")