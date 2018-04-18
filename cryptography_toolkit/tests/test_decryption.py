import unittest
import random
import string
from cryptography_toolkit import decryption as de
from cryptography_toolkit import encrpytion as en


class DecryptionTest(unittest.TestCase):
    @staticmethod
    def random_string():
        return ''.join([random.choice(string.ascii_lowercase + string.digits) for x in range(random.randint(10, 30))])

    def test_caesar_decrypt(self):
        for i in range(3):
            test_str = DecryptionTest.random_string()
            key = random.randint(1, 25)
            self.assertEqual(test_str, de.caesar_decrypt(en.caesar_cipher(test_str, key), key))

    def test_transposition_decrypt(self):
        for i in range(3):
            test_str = DecryptionTest.random_string()
            key = random.randint(3, 9)
            self.assertEqual(test_str, de.transposition_decrypt(en.transposition_cipher(test_str, key), key))


if __name__ == '__main__':
    unittest.main()
