#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """A subclass of built-in list class that adds a print_sorted method"""

    def print_sorted(self):
        """Print a list in ascending order."""
        sorted_list = sorted(self)
        print(sorted(self))
