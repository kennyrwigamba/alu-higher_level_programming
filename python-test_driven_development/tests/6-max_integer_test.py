#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        self.assertIsNone(max_integer())

    def test_one_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 9, 2, 3]), 9)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_sign_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([2, 5, 5, 1]), 5)

    def test_floats(self):
        self.assertAlmostEqual(max_integer([1.5, 2.3, 0.1]), 2.3)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_mixed_types_raises(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2"])

    def test_none_raises(self):
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
