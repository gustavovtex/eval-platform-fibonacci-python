import unittest

from numkit.factorial import factorial


class FactorialTest(unittest.TestCase):
    def test_zero_and_one(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_small_integers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_large_integer_is_exact(self):
        self.assertEqual(factorial(25), 15511210043330985984000000)

    def test_rejects_non_integers_with_type_error(self):
        for value in (1.5, "3", None, True):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    factorial(value)

    def test_rejects_negative_with_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
