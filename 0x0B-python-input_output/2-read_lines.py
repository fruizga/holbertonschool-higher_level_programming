#!/usr/bin/python3
"""read n lines of a text file (UTF8) and print it to stdout:
"""


def read_lines(filename="", nb_lines=0):
    counter = 0
    with open(filename, mode='r', encoding="utf-8") as a_File:
        for line in a_File:
                counter += 1
                print(line, end='')
                if nb_lines == counter:
                    break
