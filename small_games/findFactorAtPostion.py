from math import isqrt
from sympy import divisors, Integer

def find_factor_at_position(number, position):
    # Convert the number to a BigInteger
    number = Integer(number)

    # Check if the number is negative or zero
    if number <= 0:
        return 0

    # Get the factors of the number
    factors = sorted(divisors(number))
    print("factors: ", factors)

    # Check if the position is out of bounds
    if position < 1 or position > len(factors):
        return 0

    # Return the factor at the specified position
    return factors[position - 1]

# Example usage:
number = 97
position = 3
result = find_factor_at_position(number, position)
print(result)
