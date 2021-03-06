#!/usr/bin/python3
"""adds two integers and returns sum of numbers a & b.
"""


def add_integer(a, b=98):

    """add_integer: addition
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    add = int(a) + int(b)
    return add
