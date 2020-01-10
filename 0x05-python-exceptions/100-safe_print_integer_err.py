#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as The_Error:
        stderr.write("Exception: {}\n".format(The_Error))
        return (False)
    return (True)
