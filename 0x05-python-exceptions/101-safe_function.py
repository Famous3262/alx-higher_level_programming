#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely and return its result.

    Args:
        fct: A pointer to the function to execute.
        args: Arguments to pass to the function

    Returns:
        If an error occurs - None.
        Otherwise - the result of the function if it complete successfully.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as e
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
