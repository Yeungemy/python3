def reversed_str(str):
    result = ''
    for c in str:
        result = c + result
    return result

def palindrome(string):
    result = ''
    new_string = string.replace(' ', '')
    # result = ''.join(reversed(new_string))
    # result = new_string[::-1]
    result = reversed_str(string)
    
    if new_string == result:
        return 'It is plindrome'


print(palindrome("nurses run"))