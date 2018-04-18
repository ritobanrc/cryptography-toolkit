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
    # Dear Future Me, if you are reading this code, that means something must have gone horribly wrong.
    # Please don't do this. What I'm doing here is a terrible hack.
    plaintext = ''
    ciphertext = list(ciphertext)
    exclude_count = key * m - len(ciphertext)
    for i in range(exclude_count):
        ciphertext.insert(len(ciphertext) - m * i, '')
    for i in range(len(ciphertext)):
        # 0, 4, 8, 12, ... 28, 1,
        plaintext += ciphertext[(i % key) * m + floor(i/key)]
    return plaintext



if __name__ == '__main__':
    input_text = input('Ciphertext: ')
    print(transposition_decrypt(input_text, 8))