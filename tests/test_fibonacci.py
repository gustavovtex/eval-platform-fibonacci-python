import unittest

from numkit.fibonacci import fibonacci


class FibonacciTest(unittest.TestCase):
    def test_zero_and_one(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_first_numbers(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual([fibonacci(n) for n in range(len(expected))], expected)

    def test_large_values_are_exact(self):
        self.assertEqual(fibonacci(78), 8944394323791464)
        self.assertEqual(fibonacci(100), 354224848179261915075)

    def test_rejects_non_integers_with_type_error(self):
        for value in (1.5, "3", None, True):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    fibonacci(value)

    def test_rejects_negative_with_value_error(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)


if __name__ == "__main__":
    unittest.main()
