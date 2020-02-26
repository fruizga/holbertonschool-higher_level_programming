#!/usr/bin/python3
"""Rectangle
"""

Base = __import__('base').Base
"""Inherits from base
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height