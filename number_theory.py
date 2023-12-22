# Useful number theory functions

# Finds the Greatest Common Divisor (gcd) of two numbers using recursion
def gcd_recursion(a, b):
    """
    :param a: first number
    :param b: second number
    :return: gcd of a and b
    """
    if b == 0:
        return a
    return gcd(b, a % b)

# Finds the Greatest Common Divisor (gcd) of two numbers using the Euclidian Algorithm
def gcd(a, b):
    """
    :param a: first number
    :param b: second number
    :return: gcd of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a

# Finds the multiplicative inverse of a number 'a' mod d. This is the number 'a^-1' such that (a * a^-1) % d = 1
# This function is only valid if a and d are relatively prime (gcd(a, d) == 1)
# This function is O(d), so it is not efficient for large d
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

# Finds the modular exponentiation of a number 'x' to the power of 'exp' mod n. This is the number 'y' such that (x^exp) % n = y
def fast_modular_exponentiation(x, exp, n):
    """
    :param x: base
    :param exp: exponent
    :param n: domain size
    :return: (x^exp) % n
    """
    i = 1
    powers_of_two = [1] # powers_of_two[i] == 2^(i)
    modular_equivalences = [x%n] # modular_equivalences[i] == (x^(2^i)) % n
    while i < exp:
        i *= 2
        powers_of_two.append(i)
        modular_equivalences.append((modular_equivalences[-1]**2) % n)
    
    result = 1
    i = len(powers_of_two) - 1
    while exp > 0:
        if exp >= powers_of_two[i]:
            exp -= powers_of_two[i]
            result = (result * modular_equivalences[i]) % n
        i -= 1
        
    return result
    

## Some Test Cases ##
'''
print(gcd(66, 99)) # expect 33
print(multiplicative_inverse(2101, 2513)) # expect 1226
print(multiplicative_inverse(21017, 25139)) # expect 11118
print(fast_modular_exponentiation(25, 22, 37)) # expect 16
print(fast_modular_exponentiation(3, 70, 1003)) # expect 559
print(fast_modular_exponentiation(3, 1000000, 17)) # expect 1
print(fast_modular_exponentiation(123, 456, 789)) # expect 699
'''