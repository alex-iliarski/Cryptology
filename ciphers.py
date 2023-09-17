# Implementing simple ciphers

import number_theory as nt

# A = 65 ... Z = 90
A_ASCII = 65

# It is typical to display the ciphertext in blocks of 5 characters
def split_string(string, length = 5):
    """
    :param string: string to split
    :param length: length of each split
    :return: string with spaces every length characters
    """
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))

def ceaser_encode(str, k):
    """
    :param str: string to encode
    :param k: key
    :return: encoded string
    """
    str = str.upper()
    encoded = ""
    for c in str:
        if(not c.isalpha()): # Ignore space, special characters, etc.
            continue

        encoded_num = ((ord(c) + k - A_ASCII) % 26) + A_ASCII
        encoded += chr(encoded_num)
    return split_string(encoded)

def ceaser_decode(str, k):
    """
    :param str: string to decode
    :param k: key
    :return: decoded string
    """
    str = str.upper()
    return ceaser_encode(str, -k % 26) # Decoding is just encoding with the inverse key

# Note: the affine cipher only produces usable encodings for a=1,3,5,7,9,11,15,17,19,21,23,25
def affine_encode(str, a, b):
    """
    :param str: string to encode
    :param a: key
    :param b: key
    """
    str = str.upper()
    encoded = ""
    for c in str:
        if(not c.isalpha()): # Ignore space, special characters, etc.
            continue

        encoded_num = ((a * (ord(c) - A_ASCII) + b) % 26) + A_ASCII
        encoded += chr(encoded_num)
    return split_string(encoded)

def affine_decode(str, a, b):
    """
    :param str: string to decode
    :param a: key
    :param b: key
    """
    a_inverse = nt.multiplicative_inverse(a, 26)
    if(a_inverse == None):
        return None

    str = str.upper()
    return affine_encode(str, a_inverse, -1*a_inverse*b) # Decoding is just encoding with the inverse key
