"""Binary Search"""
import unittest
from typing import List, Any


class BinarySearch:
    """Binary Search"""
    def __init__(self) -> None:
        pass

    def binary_search(self, array: List[Any], target: Any):
        """
        Perform binary search on the given array to find the target value.

        Pseudocode:
        1. low = 1, high = n
        2. while low <= high
        3.     mid = [low + high] / 2
        4.     if A[mid] == key
        5.         return mid
        6.     if A[mid] > key
        7.         high = mid - 1
        8.     else
        9.        low = mid + 1
        10. return -1 (indicating target not found).

        Args:
            array (list): The list to search.
            target (Any): The value to search for.

        Returns:
            int: The index of the target value if found, otherwise -1.
        """
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] == target:
                return mid
            if array[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


class TestBinarySearch(unittest.TestCase):
    """Test class Binary Search."""
    def setUp(self):
        """Function to init object."""
        self.search = BinarySearch()

    def test_empty_list(self):
        """Test case for empty input."""
        self.assertEqual(self.search.binary_search([], 5), -1)

    def test_search_found(self):
        """Test case for element found."""
        self.assertEqual(self.search.binary_search([ 1, 2, 3, 4, 5 ], 3), 2)
        self.assertEqual(self.search.binary_search([ 1.1, 2.2, 3.3, 4.4, 5.5 ], 2.2), 1)
        self.assertEqual(self.search.binary_search([ 'a', 'b', 'c', 'd', 'e' ], 'e'), 4)

    def test_search_not_found(self):
        """Test case for element not present."""
        self.assertEqual(self.search.binary_search([ 1, 2, 3, 4, 5 ], 0), -1)
        self.assertEqual(self.search.binary_search([ 1.1, 2.2, 3.3, 4.4, 5.5 ], 8.1), -1)
        self.assertEqual(self.search.binary_search([ 'a', 'b', 'c', 'd', 'e' ], 'v'), -1)

    def test_search_first_element(self):
        """Test case for first element."""
        self.assertEqual(self.search.binary_search([ 1, 2, 3, 4, 5 ], 1), 0)
        self.assertEqual(self.search.binary_search([ 1.1, 2.2, 3.3, 4.4, 5.5 ], 1.1), 0)
        self.assertEqual(self.search.binary_search([ 'a', 'b', 'c', 'd', 'e' ], 'a'), 0)

    def test_search_last_element(self):
        """Test case for last element."""
        self.assertEqual(self.search.binary_search([ 1, 2, 3, 4, 5 ], 5), 4)
        self.assertEqual(self.search.binary_search([ 1.1, 2.2, 3.3, 4.4, 5.5 ], 5.5), 4)
        self.assertEqual(self.search.binary_search([ 'a', 'b', 'c', 'd', 'e' ], 'e'), 4)


if __name__ == "__main__":
    unittest.main()
