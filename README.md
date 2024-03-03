# PythonProgramming

## Algorithms

| S.No. | Algorithm                                                    | Category     |
|-------|--------------------------------------------------------------|--------------|
| 1.    |[Linear Search](/algorithms/linear_search.py)                 | Searching    |
| 2.    |[Binary Search](/algorithms/binary_search.py)                 | Searching    |
| 3.    |[Bubble Sort](/algorithms/)                                   | Sorting      |
| 4.    |[Selection Sort](/algorithms/)                                | Sorting      |
| 5.    |[Insertion Sort](/algorithms/)                                | Sorting      |
| 6.    |[Merge Sort]()                                                |              |
| 7.    |[Quick Sort]()                                                |              |
| 8.    |[Heap Sort]()                                                 |              |
| 9.    |[Count Sort]()                                                |              |
| 10.   |[Radix Sort]()                                                |              |
| 11.   |[Bucket Sort]()                                               |              |
|       |                                                              |              |
|       |                                                              |              |

1. Linear Search

```
1. for i = 1 to n
2. if A[i] == key
3.     return i
4. return -1 (indicating target not found).
```

2. Binary Search

```
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
```


## Data Structures

