import unittest
from cryptography_toolkit import encrpytion as en


class EncryptionTest(unittest.TestCase):
    def test_reverse_cipher(self):
        self.assertEqual(en.reverse_cipher("Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
                         ".tile gnicsipida rutetcesnoc ,tema tis rolod muspi meroL")

    def test_caesar_cipher(self):
        self.assertEqual(en.caesar_cipher("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 7),
                         "svylt pwzbt kvsvy zpa htla, jvuzljalaby hkpwpzjpun lspa.")

    def test_transposition_cipher(self):
        self.assertEqual(en.transposition_cipher("Common sense is not so common.", 8), "Cenoonommstmme oo snnio. s s c")

    def test_rot13(self):
        self.assertEqual(en.rot13_cipher("Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
                         "yberz vcfhz qbybe fvg nzrg, pbafrpgrghe nqvcvfpvat ryvg.")


if __name__ == '__main__':
    unittest.main()
