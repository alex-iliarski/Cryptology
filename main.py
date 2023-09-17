# Main Runner for testing ciphers and number theory functions

import ciphers
import number_theory as nt

def main():
    ## Test Ceaser Cipher
    print('\nTesting Ceaser Cipher::\n')
    s = 'This is a test of the Ceaser Cipher!'
    a = 1
    print('The message is: ' + s)

    encrypted = ciphers.ceaser_encode(s, a)
    print('The cyphertext is: ' + encrypted)

    decrypted = ciphers.ceaser_decode(encrypted, a)
    print('The decrypted message is: ' + decrypted)

    print('\n-------------------\n')

    ## Test Affine Cipher
    print('Testing Affine Cipher::\n')
    s = 'Hello World! It is a beautiful day!'
    a = 15
    b = 18
    print('The message is: ' + s)

    encrypted = ciphers.affine_encode(s, a, b)
    print('The cyphertext is: ' + encrypted)

    decrypted = ciphers.affine_decode(encrypted, a, b)
    print('The decrypted message is: ' + decrypted)

main()