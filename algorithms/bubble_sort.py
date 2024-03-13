"""Bubble Sort"""
import unittest
from typing import List, Any


class BubbleSort:
    """Bubble Sort"""
    def __init__(self) -> None:
        self._iterations = 0
        self._swaps = 0

    def bubble_sort(self, array: List[Any]) -> List[Any]:
        """
        Perform bubble sort on the input array to sort in ascending order.
        Iteratively compares adjacent elements and swaps them if they are in the wrong order
        until the list is sorted.

        Pseudocode:
        1. for i = 1 to n - 1
        2.     for j = 1 to n - i - 1
        3.         if A[j] > A[j + 1]
        4.             exchange A[j] with A[j + 1]

        Args:
            array (list): The list to sort.

        Returns:
            array (list): The list in sorted order.
        """
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                self._iterations += 1 # for debug analyse
                if array[j] > array[j + 1]:
                    self._swaps += 1  # for debug analyse
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    def analyse_algorithm(self):
        """Calculate num of swaps and iterations."""
        print(f"{BubbleSort.__doc__}: {self._iterations} iterations and {self._swaps} swaps.")


class TestBubbleSort(unittest.TestCase):
    """Test class Bubble Sort."""
    def setUp(self):
        """Function to init object."""
        self.sort = BubbleSort()

    def test_empty_list(self):
        """Test case for empty input."""
        self.assertEqual(self.sort.bubble_sort([]), [])

    def test_sort_basic(self):
        """Test case for basic sort."""
        self.assertEqual(self.sort.bubble_sort([3, 2, 4, 5, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(self.sort.bubble_sort([4.4, 2.2, 1.1, 3.3, 5.5]),
                                                [1.1, 2.2, 3.3, 4.4, 5.5])
        self.assertEqual(self.sort.bubble_sort(['c', 'a', 'b', 'e', 'd']),
                                                ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(self.sort.bubble_sort([-5, -8, -3, -1, -9]), [-9, -8, -5, -3, -1])

    def test_sort_sorted(self):
        """Test case for already sorted."""
        self.assertEqual(self.sort.bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(self.sort.bubble_sort([1.1, 2.2, 3.3, 4.4, 5.5]),
                                                [1.1, 2.2, 3.3, 4.4, 5.5])
        self.assertEqual(self.sort.bubble_sort([-9, -8, -5, -3, -1]), [-9, -8, -5, -3, -1])

    def test_sort_repeated(self):
        """Test case for repeated elements."""
        self.assertEqual(self.sort.bubble_sort([3, 3, 4, 5, 1]), [1, 3, 3, 4, 5])
        self.assertEqual(self.sort.bubble_sort([4.4, 2.2, 1.1, 1.1, 5.5]),
                                                [1.1, 1.1, 2.2, 4.4, 5.5])
        self.assertEqual(self.sort.bubble_sort(['c', 'a', 'b', 'e', 'e']),
                                                ['a', 'b', 'c', 'e', 'e'])
        self.assertEqual(self.sort.bubble_sort([-8, -8, -3, -1, -5]), [-8, -8, -5, -3, -1])

    def test_sort_same_element(self):
        """Test case for sorting same element."""
        self.assertEqual(self.sort.bubble_sort([1, 1, 1, 1, 1]),[1, 1, 1, 1, 1])
        self.assertEqual(self.sort.bubble_sort([0.7, 0.7, 0.7, 0.7, 0.7]),
                                                [0.7, 0.7, 0.7, 0.7, 0.7])
        self.assertEqual(self.sort.bubble_sort(['r', 'r', 'r', 'r', 'r']),
                                                ['r', 'r', 'r', 'r', 'r'])


if __name__ == "__main__":
    unittest.main()
