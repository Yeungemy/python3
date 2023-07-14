def up_low_case_check(my_str):
    num_of_up = 0
    num_of_low = 0

    for letter in my_str:
        if letter.isupper() == True:
            num_of_up += 1
        else:
            num_of_low += 1

    print(f'No. of Upper case characters : {num_of_up}')
    print(f'No. of Lower case characters : {num_of_low}')


up_low_case_check('This iS mY, Test String')