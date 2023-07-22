from random import randint
import pdb

def fibon(rangeNum):
    a = 1 
    b =1 

    for i in range(rangeNum):
        yield a
        a, b = b, a + b

def print_fibon(rangeNum):
    for i in fibon(rangeNum):
        print(i)

# print(list(fibon(10)))
# print_fibon(10)

def random_num(low, high, n):
    for i in range(n):
        yield randint(low, high)

def print_random_num(low, high, n):
    for i in random_num(low, high, n):
        print(i)

# print_random_num(1, 10, 5)


def print_string():
    s = iter('Hello')

    for i in s:
        pdb.set_trace()
        print(i)

print_string()

        