#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer and return, True if value is an integer.

    Args:
        value (int): The integer to print.

    Returns:
        True - if value is an integer and has been printed.
        False - otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
