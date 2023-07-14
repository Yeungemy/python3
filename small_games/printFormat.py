my_string = 'tinker'

# Strings are not mutable! (meaning you can't use indexing to change individual elements of a string) 
# my_string[0] = 'x'

# start the second character and stop the fifth but not include
print(my_string[1:4]) #tink

# from the beginning and stop to the fourth but not include
print(my_string[:4]) # tink

# slice characters by step 3
print(my_string[::3]) # tk

# reverse the string
print(my_string[::-1])

print(my_string * 10) # tinkertinkertinkertinkertinkertinkertinkertinkertinkertinker

print('2' + '3') # 23

print(2 + 3)  # 5

print(my_string.split('i')) #['t', 'nker']

print('This is a string {}'.format('INSERTED')) # This is a string INSERTED

print('The {} {} {}'.format('fox', 'brown', 'quick')) # the fox brown quick

print('The {q} {b} {f}'.format(f ='fox', b ='brown', q ='quick')) # the quick brown fox 

print('The {2} {1} {0}'.format('fox', 'brown', 'quick')) # the quick brown fox

print('The {0} {0} {0}'.format('fox', 'brown', 'quick')) # the fox fox fox

# float formatting follows "{value:width.precision f}" width is the white space

result = 10000/23

print('The result was {r:1.3f}'.format(r = result)) # The result was 434.783

name = 'Jose'
print(f'Hello, my name is {name}') # f_string: Hello, my name is Jose

list = ['a','b','c'][1:]
print(f'{list}') # ['b', 'c']

myfile = open('myfile.txt')
content = myfile.read()
print(f'\n{content}')

myfile.seek(0)

myfile = open('myfile.txt')
content = myfile.readlines()
print(f'\n{content}')

myfile.seek(0)

myfile = open('myfile.txt')
content = myfile.readline()
print(f'\n{content}')

#close the file
myfile.close()

with open('myfile.txt') as my_file:
    content = my_file.readlines()
    print(f'\n{content}')

with open('myfile.txt', mode = 'a') as f:
    f.write('\nNew line added on')

with open('myfile.txt', mode = 'r') as f:
    print(f.read())

with open('myfileNew.txt', mode = 'w') as f:
    f.write('This is my new file')

with open('myfileNew.txt', mode = 'r') as f:
    print(f.read())