#prompt for a year
test_year = int(input("Please enter a year: "))
remainder_4_division = test_year % 4
remainder_100_division = test_year % 100
remiander_400_division = test_year % 400

print(f"The reminder of 4 is {remainder_4_division}")
print(f"The reminder of 100 is {remainder_100_division}")
print(f"The reminder of 400 is {remiander_400_division}")

if remainder_4_division == 0:
    if remainder_100_division == 0:
        if remiander_400_division == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")