height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round((weight / height**2), 2)
BMI_final = float("{:.2f}".format(BMI))

print(f"Your BMI is {BMI_final}")

if BMI_final < 18.5:
  print("You are underweight")
elif BMI_final < 25:
  print("You are normalweight")
elif BMI_final < 30:
  print("You are overweight")
elif BMI_final < 35:
  print("You are obese")
else:
  print("You are clinically obese")