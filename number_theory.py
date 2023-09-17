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

# Finds the multiplicative inverse of a number 'a' mod d. This is the number 'a^-1' such that (a * a^-1) % d = 1
def multiplicative_inverse(a, d):
    """
    :param a: number to find inverse of
    :param d: domain size
    :return: a^-1, the multiplicative inverse of a in domain d
    """
    for i in range(d):
        if (a * i) % d == 1:
            return i
    return None

#print(gcd(100, 99))
#print(multiplicative_inverse(3, 26))