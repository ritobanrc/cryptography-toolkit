import string
import sys

ALPHABET = string.ascii_lowercase

def l2n(l):
    if l in ALPHABET:
        return ALPHABET.index(l)
    print(l, " not in alphabet. Usage: l2n(letter)", file=sys.stderr)


def n2l(n):
    if n >= len(ALPHABET):
        print(n, " is greater that the alphabet size. Usage n2l(number)", file=sys.stderr)
        return
    return ALPHABET[n]