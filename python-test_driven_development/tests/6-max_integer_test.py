#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test with ordered list"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test with unordered list"""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test with max value at beginning"""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_max_at_end(self):
        """Test with max value at end"""
        max_at_end = [1, 2, 3, 4]
        self.assertEqual(max_integer(max_at_end), 4)

    def test_single_element(self):
        """Test with single element list"""
        single = [5]
        self.assertEqual(max_integer(single), 5)

    def test_empty_list(self):
        """Test with empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        negative = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative), -1)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        mixed = [-1, 2, -3, 4]
        self.assertEqual(max_integer(mixed), 4)

    def test_float_numbers(self):
        """Test with float numbers"""
        floats = [1.5, 2.7, 3.1, 4.9]
        self.assertEqual(max_integer(floats), 4.9)

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        duplicates = [1, 4, 3, 4]
        self.assertEqual(max_integer(duplicates), 4)

    def test_all_same_values(self):
        """Test with all same values"""
        same = [3, 3, 3, 3]
        self.assertEqual(max_integer(same), 3)

    def test_large_numbers(self):
        """Test with large numbers"""
        large = [1000000, 2000000, 3000000]
        self.assertEqual(max_integer(large), 3000000)

    def test_zero_in_list(self):
        """Test with zero in list"""
        with_zero = [0, 1, 2, 3]
        self.assertEqual(max_integer(with_zero), 3)

    def test_all_zeros(self):
        """Test with all zeros"""
        all_zeros = [0, 0, 0, 0]
        self.assertEqual(max_integer(all_zeros), 0)

    def test_one_negative(self):
        """Test with one negative number"""
        one_negative = [-5]
        self.assertEqual(max_integer(one_negative), -5)

    def test_strings_in_list(self):
        """Test with strings in list (should work with comparison)"""
        strings = ["a", "b", "c", "d"]
        self.assertEqual(max_integer(strings), "d")


if __name__ == '__main__':
    unittest.main()
