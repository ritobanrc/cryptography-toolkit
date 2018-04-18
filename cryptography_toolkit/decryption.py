from cryptography_toolkit.encrpytion import reverse_cipher, caesar_cipher, rot13_cipher
from math import floor, ceil


def reverse_decrypt(ciphertext):
    return reverse_cipher(ciphertext)


def caesar_decrypt(ciphertext, key):
    return caesar_cipher(ciphertext, 26-key)


def rot13_decrypt(ciphertext):
    return rot13_cipher(ciphertext)


def transposition_decrypt(ciphertext, key):
    m = ceil(len(ciphertext)/key)
    plaintext = [''] * m * key
    for i in range(len(ciphertext)):
        '''
        Issue: the grey boxes
        
        '''
        plaintext[(i % m) * key + floor(i/m)] = ciphertext[i]
    return ''.join(plaintext)


if __name__ == '__main__':
    input_text = input('Ciphertext: ')
    print(transposition_decrypt(input_text, 8))