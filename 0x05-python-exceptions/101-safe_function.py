#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as The_Error:
        stderr.write("Exception: {}\n".format(The_Error))
        return (None)
