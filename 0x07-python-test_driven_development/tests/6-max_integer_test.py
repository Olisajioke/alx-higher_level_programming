import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Should return None for an empty list")

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5, "Should return the single element in the list")

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 7, 2, 9]), 9, "Should return the maximum positive number")

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -9, -1]), -1, "Should return the maximum negative number")

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 5, -8]), 5, "Should return the maximum mixed number")

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3, "Should return the maximum number for duplicate values")

    def test_mixed_numbers_with_zero(self):
        self.assertEqual(max_integer([0, 1, -2, 5, -8]), 5, "Should return the maximum mixed number including zero")

    def test_large_numbers(self):
        self.assertEqual(max_integer([10**6, 10**9, 10**12]), 10**12, "Should handle large numbers")

    def test_mixed_large_numbers(self):
        self.assertEqual(max_integer([10**6, -10**9, 10**12, -10**15]), 10**12, "Should handle mixed large numbers")

    def test_unordered_list(self):
        self.assertEqual(max_integer([3, 1, 5, 2]), 5, "Should handle an unordered list")

    def test_max_number_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 3, 7, 2]), 9, "Should handle the maximum number at the beginning of the list")

    def test_max_number_at_end(self):
        self.assertEqual(max_integer([3, 1, 2, 7, 9]), 9, "Should handle the maximum number at the end of the list")

    def test_negative_max_number(self):
        self.assertEqual(max_integer([-3, -1, -2, -7, -9]), -1, "Should handle the maximum negative number")

    def test_max_number_in_middle(self):
        self.assertEqual(max_integer([3, 1, 9, 2, 5]), 9, "Should handle the maximum number in the middle of the list")

    def test_max_number_multiple_occurrences(self):
        self.assertEqual(max_integer([3, 9, 3, 9, 9, 2, 5]), 9, "Should handle multiple occurrences of the maximum number")

if __name__ == '__main__':
    unittest.main()
