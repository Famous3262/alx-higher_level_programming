#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """An empty class that can be used as a base class
    for geometry-related classes.
    """

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
