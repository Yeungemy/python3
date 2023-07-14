# welcome greeting
print("Welcom to the tip calculator.")

#prompt for the amount of the bill
bill_amount = float(input("What was the total bill?\nThe toal amount of the bill is $"))
print(f"Bill is {bill_amount}");

#prompt for the percentage of the tip to give
tip_percentage = int(input("What percentage tip would you like to give, 10, 12, or 15?\nThe percentage of the tip for the bill is "))/100

#prompt for the number of the people to pay for the bill
num_of_people = int(input("How many people are going to split the bill?\nthe number of the people to split the bill is "))

#calculate the amount for each people to pay for the bill
amount_to_pay = ((bill_amount * (1 + tip_percentage)) / num_of_people)
final_amount = "{:.2f}".format(amount_to_pay)
msg_string = f"Each person should pay: ${final_amount}"

#print the amount for each person to pay for the bill
print("%.2f" % amount_to_pay)
print(msg_string)