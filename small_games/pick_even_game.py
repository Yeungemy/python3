def pick_even(*args): 
    return [num for num in args if num % 2 == 0]

print(pick_even(1, 2, 3, 4, 5))