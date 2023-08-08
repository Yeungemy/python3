from math import factorial;

def factorial_1(testNumber):
    result = 1;
    if testNumber != 0:
        for i in range(1, testNumber + 1):
            result = result * i;
    return result;

def factorial_2(teestNumber):
    factorial(teestNumber)

def factorial_3(testNumber):
    if testNumber == 0:
        return 1
    else:
        return testNumber * factorial_3(testNumber -1);

def getFactorialNumber():
    while True:
        try:
            num1 = int((input("Please enter a number: ")))
            return num1;
            break;
        except ValueError: # catch the *specific* exception 
            print("Enter numbers only")


#


print(factorial_3(getFactorialNumber()))

