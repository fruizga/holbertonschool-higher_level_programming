#!/usr/bin/python3
"""returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    counter = 0
    with open(filename, mode='r', encoding="utf-8") as a_File:
        for line in a_File:
            counter += 1
    return (counter)
