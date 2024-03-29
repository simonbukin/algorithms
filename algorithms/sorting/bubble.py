"""
sorting/bubble.py
Bubble Sort algorithm implementation

High Level Description:
For each element in the list, iterate through the remaining elements after
it and swap if the element is smaller. This 'bubbles up' the elements into
their correct indexes.

Time Complexity:
Since the algorithms iterates through every element, this uses O(n) time.
Swapping may take up to O(n/2) time, thus the overall time is O(n^2).
"""


def bubble_sort(lst):
    for i, _ in enumerate(lst):
        for j, _ in enumerate(lst[i:]):
            j += i
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
