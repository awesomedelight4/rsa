"""
test_rsa.py  —  run with:  python test_rsa.py
All 5 test groups must pass before you submit.
"""

import unittest
from rsa_exercise import gcd, is_prime, generate_keys, encrypt, decrypt


class TestGCD(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(17, 5), 1)
        self.assertEqual(gcd(100, 75), 25)

    def test_same_number(self):
        self.assertEqual(gcd(7, 7), 7)

    def test_one(self):
        self.assertEqual(gcd(1, 99), 1)


class TestIsPrime(unittest.TestCase):
    def test_primes(self):
        for n in [2, 3, 5, 7, 11, 13, 17, 97]:
            self.assertTrue(is_prime(n), f"{n} should be prime")

    def test_non_primes(self):
        for n in [0, 1, 4, 6, 9, 15, 25, 100]:
            self.assertFalse(is_prime(n), f"{n} should NOT be prime")


class TestKeyGeneration(unittest.TestCase):
    def test_key_structure(self):
        pub, priv = generate_keys(11, 17)
        e, n = pub
        d, n2 = priv
        self.assertEqual(n, n2)
        self.assertEqual(n, 187)          # 11 * 17
        self.assertEqual(gcd(e, (11-1)*(17-1)), 1)

    def test_modular_inverse(self):
        pub, priv = generate_keys(11, 17)
        e, n = pub
        d, _  = priv
        phi = (11-1)*(17-1)
        self.assertEqual((e * d) % phi, 1, "e and d must be modular inverses")

    def test_raises_on_non_prime(self):
        with self.assertRaises(ValueError):
            generate_keys(4, 17)
        with self.assertRaises(ValueError):
            generate_keys(11, 9)


class TestEncryptDecrypt(unittest.TestCase):
    def setUp(self):
        self.pub, self.priv = generate_keys(11, 17)

    def test_round_trip(self):
        msg = "HELLO"
        self.assertEqual(decrypt(encrypt(msg, self.pub), self.priv), msg)

    def test_single_char(self):
        for ch in "ABCZ":
            self.assertEqual(decrypt(encrypt(ch, self.pub), self.priv), ch)

    def test_encrypt_returns_list_of_ints(self):
        result = encrypt("HI", self.pub)
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(x, int) for x in result))

    def test_larger_primes(self):
        pub, priv = generate_keys(61, 53)
        msg = "RSA"
        self.assertEqual(decrypt(encrypt(msg, pub), priv), msg)


class TestEdgeCases(unittest.TestCase):
    def test_empty_message(self):
        pub, priv = generate_keys(11, 17)
        self.assertEqual(decrypt(encrypt("", pub), priv), "")

    def test_single_character_message(self):
        pub, priv = generate_keys(11, 17)
        self.assertEqual(decrypt(encrypt("A", pub), priv), "A")


if __name__ == "__main__":
    unittest.main(verbosity=2)
