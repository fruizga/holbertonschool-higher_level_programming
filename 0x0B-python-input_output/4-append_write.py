#!/usr/bin/python3
'''
writes to a file, if it exists it appends otherwise it creates it
'''


def append_write(filename="", text=""):
    '''
    Append to an existing file or creating a new one
    '''
    with open(filename, mode='a', encoding='utf-8') as a_File:
        return a_File.write(text)
