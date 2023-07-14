import string

def ispangram(str1, alphabet = string.ascii_lowercase):
    # create a alphabet set
    alphaset = set(alphabet)
    print(alphaset)

    # replace empty space
    str1 = str1.replace(' ', '')

    # lower all letters
    str1 = str1.lower()

    # create str set
    str1 = set(str1)
    print(str1)

    # return result
    print (alphaset == str1)

my_str = 'the quick brown fox jumps over the lazy frog'

ispangram(my_str)