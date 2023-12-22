# Main Runner for testing ciphers and number theory functions

import ciphers
import number_theory as nt

def main():
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

main()