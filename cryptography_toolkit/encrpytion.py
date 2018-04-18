from cryptography_toolkit.util import l2n, n2l, ALPHABET
from math import floor, ceil


def reverse_cipher(plaintext):
    return plaintext[::-1]


def caesar_cipher(plaintext, key, case_sensitive = False):
    if not case_sensitive:
        plaintext = plaintext.lower()
    ciphertext = ''
    for letter in plaintext:
        if letter in ALPHABET:
            ciphertext += n2l((l2n(letter) + key)%len(ALPHABET))
        else:
            ciphertext += letter
    return ciphertext


def rot13_cipher(plaintext):
    return caesar_cipher(plaintext, 13)


def transposition_cipher(plaintext, key):
    n = ceil(len(plaintext) / key)
    ciphertext = [''] * n * key
    for i in range(len(plaintext)):
        # Converts i to 2D coordinates, transposes, and converts back into 1D
        ciphertext[floor(i/key) + (i % key) * n] = plaintext[i]
    return ''.join(ciphertext)



if __name__ == '__main__':
    input_text = input("Plaintext: ")
    print(transposition_cipher(input_text, 8))