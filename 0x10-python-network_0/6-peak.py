#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    size = len(list_of_integers)
    lo = hi_size
    mid = hi_size // 2

    if hi_size == 0:
        return None

    while True:
        lo = lo // 2
        if (mid < hi_size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if lo // 2 == 0:
                lo = 2
            mid = mid + lo // 2
        elif lo > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if lo // 2 == 0:
                lo = 2
            mid = mid - lo // 2
        else:
            return list_of_integers[mid]
