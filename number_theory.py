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
    
# Finds a factor of the given integer using Pollard's rho algorithm. O(p^0.5), where p is a factor of n
def pollard_rho(n):
    """
    :param n: integer to find a factor of
    :return: a non-trivial factor of n
    """
    def f(x): # f(x) = (x^2 + 2) mod n
        # Note: Other f(x) functions can be used, but this one is simple and works well for most cases
        return (x**2 + 2) % n
    x = 2 # x_0 = 2
    y = 2
    gcd_result = 1
    while gcd_result == 1: # continue until gcd is non-trivial
        x = f(x) # x_k = f(x_k-1)
        y = f(f(y)) # y_k = x_2k = f(f(y_k-1))
        gcd_result = gcd(abs(x - y), n)
    return gcd_result

# Verifies if the result attained from pollard_rho is correct
def test_pollard_rho(n, res):
    """
    :param n: integer to find a factor of
    :param res: result attained from pollard_rho
    """
    print('According to Pollard Rho, a factor of ' + str(n) + ' is: ' + str(res))
    print('Check that it is a factor: ' + str(n % res == 0))

## Some Test Cases ##
'''
print(gcd(66, 99)) # expect 33

print(multiplicative_inverse(2101, 2513)) # expect 1226
print(multiplicative_inverse(21017, 25139)) # expect 11118

print(fast_modular_exponentiation(25, 22, 37)) # expect 16
print(fast_modular_exponentiation(3, 70, 1003)) # expect 559
print(fast_modular_exponentiation(3, 1000000, 17)) # expect 1
print(fast_modular_exponentiation(123, 456, 789)) # expect 699

n = 13*277 # n is a semiprime number
res = pollard_rho(n)
test_pollard_rho(n, res)

n = 43943*44119 # n is a large semiprime number
res = pollard_rho(n)
test_pollard_rho(n, res)

n = 2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17 # n is a large composite number
res = pollard_rho(n)
test_pollard_rho(n, res)
'''
