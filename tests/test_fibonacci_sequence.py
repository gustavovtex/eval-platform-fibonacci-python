import unittest

from numkit.fibonacci import MAX_SEQUENCE_LENGTH, fibonacci, fibonacci_sequence


class FibonacciSequenceTest(unittest.TestCase):
    def test_zero_is_empty(self):
        self.assertEqual(fibonacci_sequence(0), [])

    def test_first_numbers(self):
        self.assertEqual(fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_every_term_matches_fibonacci(self):
        sequence = fibonacci_sequence(200)
        self.assertEqual(len(sequence), 200)
        for n, term in enumerate(sequence):
            self.assertEqual(term, fibonacci(n))

    def test_accepts_the_cap_and_rejects_beyond_it(self):
        self.assertEqual(MAX_SEQUENCE_LENGTH, 10000)
        self.assertEqual(len(fibonacci_sequence(10000)), 10000)
        with self.assertRaises(ValueError):
            fibonacci_sequence(10001)

    def test_validates_count(self):
        for value in (1.5, "3", None, True):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    fibonacci_sequence(value)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)


if __name__ == "__main__":
    unittest.main()
