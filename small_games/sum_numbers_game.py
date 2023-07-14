# learn *args and **kwargs
def sun_numbers(a, b, c = 0, d= 0):
    print (sum((a, b, c, d)) * 0.05)

def sum_unlimited_numbers(*args):
    print(sum(args)* 0.05)

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like to {} {}'.format(args[0], kwargs['food']))

sun_numbers(1, 2, 3, 4)
sum_unlimited_numbers(1, 2, 3, 4, 5, 6, 7)
myfunc(10, 20, 30, fruit = "orange", food = 'eggs', animal = 'dog')