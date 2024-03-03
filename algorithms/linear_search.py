""" Module providing unit tests. """
import unittest
from typing import List, Any


class LinearSearch:
    """ Linear Search """
    def __init__(self) -> None:
        pass

    def linear_search(self, array: List[Any], target: Any) -> int:
        """
        Perform linear search on the given array to find the target value.

        Pseudocode:
        1. for i = 1 to n
        2. if A[i] == key
        3.     return i
        4. return -1 (indicating target not found).

        Args:
            array (list): The list to search.
            target (Any): The value to search for.

        Returns:
            int: The index of the target value if found, otherwise -1.
        """
        for i, element in enumerate(array):
            if element == target:
                return i
        return -1


class TestLinearSearch(unittest.TestCase):
    """ Test class Linear Search. """
    def setUp(self):
        """ Function to init object. """
        self.search = LinearSearch()

    def test_empty_list(self):
        """ Test case for empty input. """
        self.assertEqual(self.search.linear_search([], 5), -1)

    def test_search_found(self):
        """ Test case for element found. """
        self.assertEqual(self.search.linear_search([1, 4, 6, 9, 2, 5], 9), 3)
        self.assertEqual(self.search.linear_search([0.4, 4.2, 3.8, 6.1, 2.7, 5.5], 6.1), 3)
        self.assertEqual(self.search.linear_search(['b', 's', 'a', 'r', 's', 'o'], 'a'), 2)

    def test_search_not_found(self):
        """ Test case for element not present. """
        self.assertEqual(self.search.linear_search([1, 4, 6, 9, 2, 5], 0), -1)
        self.assertEqual(self.search.linear_search([0.4, 4.2, 3.8, 6.1, 2.7, 5.5], 2.1), -1)
        self.assertEqual(self.search.linear_search(['b', 's', 'a', 'r', 's', 'o'], 'z'), -1)

    def test_search_first_element(self):
        """ Test case for first element. """
        self.assertEqual(self.search.linear_search([1, 4, 6, 9, 2, 5], 1), 0)
        self.assertEqual(self.search.linear_search([0.4, 4.2, 3.8, 6.1, 2.7, 5.5], 0.4), 0)
        self.assertEqual(self.search.linear_search(['b', 's', 'a', 'r', 's', 'o'], 'b'), 0)

    def test_search_last_element(self):
        """ Test case for last element. """
        self.assertEqual(self.search.linear_search([1, 4, 6, 9, 2, 5], 5), 5)
        self.assertEqual(self.search.linear_search([0.4, 4.2, 3.8, 6.1, 2.7, 5.5], 5.5), 5)
        self.assertEqual(self.search.linear_search(['b', 's', 'a', 'r', 's', 'o'], 'o'), 5)


if __name__ == "__main__":
    unittest.main()
