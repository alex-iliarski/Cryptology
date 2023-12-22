# Main Runner for testing ciphers and number theory functions

import ciphers
import number_theory as nt

# Test simple ciphers
def test_ciphers():
    ## Test Ceaser Cipher
    print('\n-------------------\nTesting Ceaser Cipher::\n')
    s = 'This is a test of the Ceaser Cipher!'
    a = 1
    print('The message is: ' + s)

    encrypted = ciphers.ceaser_encode(s, a)
    print('The cyphertext is: ' + encrypted)

    decrypted = ciphers.ceaser_decode(encrypted, a)
    print('The decrypted message is: ' + decrypted)

    ## Test Affine Cipher
    print('\n-------------------\nTesting Affine Cipher::\n')
    s = 'Hello World! It is a beautiful day!'
    a = 15
    b = 18
    print('The message is: ' + s)

    encrypted = ciphers.affine_encode(s, a, b)
    print('The cyphertext is: ' + encrypted)

    decrypted = ciphers.affine_decode(encrypted, a, b)
    print('The decrypted message is: ' + decrypted)

    ## Test One Time Pad
    print('\n-------------------\nTesting One Time Pad::\n')
    s = 'The One Time Pad is a theoretically unbreakable cipher!'
    print('The message is: ' + s)

    encrypted, keys = ciphers.one_time_pad_encode(s)
    print('The cyphertext is: ' + encrypted)

    decrypted = ciphers.one_time_pad_decode(encrypted, keys)
    print('The decrypted message is: ' + decrypted)
    
    ## Test General Substitution Cipher
    print('\n-------------------\nTesting General Substitution Cipher::\n')
    s = 'Lets test out the General Substitution Cipher!'
    print('The message is: ' + s)
    encrypted, substitution_map = ciphers.general_substitution_encode(s)
    print('The cyphertext is: ' + encrypted)
    
    decrypted = ciphers.general_substitution_decode(encrypted, substitution_map)
    print('The decrypted message is: ' + decrypted)
    
# Test simple number theory functions
def test_number_theory():
    ## Test GCD
    print('\n-------------------\nTesting GCD::\n')
    a = 123456789
    b = 987654321
    print('GCD of ' + str(a) + ' and ' + str(b) + ' is: ' + str(nt.gcd(a, b)))
    
    ## Test Multiplicative Inverse
    print('\n-------------------\nTesting Multiplicative Inverse::\n')
    a = 2101
    d = 2513
    print('Multiplicative Inverse of ' + str(a) + ' mod ' + str(d) + ' is: ' + str(nt.multiplicative_inverse(a, d))) # expect 1226
    a = 21017
    d = 25139
    print('Multiplicative Inverse of ' + str(a) + ' mod ' + str(d) + ' is: ' + str(nt.multiplicative_inverse(a, d))) # expect 11118
    
    ## Test Fast Modular Exponentiation
    print('\n-------------------\nTesting Fast Modular Exponentiation::\n')
    x = 3
    exp = 70
    n = 1003
    print(str(x) + '^' + str(exp) + ' mod ' + str(n) + ' is: ' + str(nt.fast_modular_exponentiation(x, exp, n))) # expect 559
    x = 123
    exp = 456
    n = 789
    print(str(x) + '^' + str(exp) + ' mod ' + str(n) + ' is: ' + str(nt.fast_modular_exponentiation(x, exp, n))) # expect 699
    
if __name__ == "__main__":
    test_ciphers()
    test_number_theory()