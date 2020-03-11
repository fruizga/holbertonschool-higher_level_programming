#!/usr/bin/python3
'''
Writing to a file and returning the number of characters
'''


def write_file(filename="", text=""):
    '''
    Write a string to a file
    '''
    with open(filename, mode='w', encoding='utf-8') as a_File:
        return a_File.write(text)
