# Useful number theory functions

# Finds the Greatest Common Divisor (gcd) of two numbers
def gcd(a, b):
    """
    :param a: first number
    :param b: second number
    :return: gcd of a and b
    """
    if b == 0:
        return a
    return gcd(b, a % b)

# Finds the Greatest Common Divisor (gcd) of two numbers using the Euclidian Algorithm
## TODO:: Implement this
def gcd_euclidian_algorithm(a, b):
    """
    :param a: first number
    :param b: second number
    :return: gcd of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(100, 99))