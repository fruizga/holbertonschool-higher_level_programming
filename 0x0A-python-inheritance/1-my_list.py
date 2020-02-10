#!/usr/bin/python3
"""
MyList class inherits from list
"""
class MyList(list):
    def print_sorted(self):
        """
        print sorted lista
        """
        print(sorted(self))
