# Implementing simple ciphers
import os
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

def one_time_pad_encode(str):
    """
    :param str: string to encode
    :param keys: list of keys
    :return: Pair of encoded string and keys needed to decode the string
    """
    str = str.upper()
    str = "".join(c for c in str if c.isalpha()) # Remove all non-alphabetic characters from string
    keys = generate_one_time_pad_keys(len(str))
    encoded = ""
    for i in range(len(str)):
        encoded_num = ((ord(str[i]) + keys[i] - A_ASCII) % 26) + A_ASCII
        encoded += chr(encoded_num)
    return (split_string(encoded), keys)

def one_time_pad_decode(str, keys):
    """
    :param str: string to decode
    :param keys: list of keys
    :return: decoded string
    """
    str = str.upper()
    str = "".join(c for c in str if c.isalpha()) # Remove all non-alphabetic characters from string
    decoded = ""
    for i in range(len(str)):
        if(not str[i].isalpha()): # Ignore space, special characters, etc.
            continue

        decoded_num = ((ord(str[i]) - keys[i] - A_ASCII) % 26) + A_ASCII
        decoded += chr(decoded_num)
    return split_string(decoded)

def generate_one_time_pad_keys(length):
    """
    :param length: length of key to generate
    :return: list of keys
    """
    return [ord(os.urandom(1)) % 26 for i in range(length)]

# General Substitution Cipher
def general_substitution_encode(str):
    """
    :param str: string to encode
    :return: Tuple of encoded string and mapping of letters
    """
    map = create_substitution_map()
    str = str.upper()
    str = "".join(c for c in str if c.isalpha()) # Remove all non-alphabetic characters from string
    encoded = ""
    for c in str:
        encoded += map[c]
    return (split_string(encoded), map)
    
    
def create_substitution_map():
    """
    :return: unique mapping of letters
    """
    # Create unique mapping of letters to a new letter with no repeats
    map = {}
    letters = [chr(i) for i in range(A_ASCII, A_ASCII + 26)]
    letters_copy = letters.copy()
    
    for c in letters:
        map[c] = letters_copy.pop(ord(os.urandom(1)) % len(letters_copy))
    
    return map

def general_substitution_decode(str, map):
    """
    :param str: string to decode
    :param map: mapping of letters
    :return: decoded string
    """
    str = str.upper()
    str = "".join(c for c in str if c.isalpha()) # Remove all non-alphabetic characters from string
    decoded = ""
    
    # Create a reverse mapping by swapping keys and values in the map dictionary
    reverse_map = {v: k for k, v in map.items()}
    
    for c in str:
        if c in reverse_map:
            decoded += reverse_map[c]
        else:
            # If the character is not found in the map, keep it as is
            decoded += c
            
    return split_string(decoded)
