#!/usr/bin/python3
"""Rectangle
"""

from models.base import Base
"""Inherits from base
"""


class Rectangle(Base):
    """jejejeje"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """jijiji"""
        return self.__width

    @width.setter
    def width(value):
        """jojojo"""
        self.__width = value

    @property
    def height(self):
        """height get"""
        return self.__height

    @height.setter
    def height(value):
        """other"""
        self.__height = value

    @property
    def x(self):
        """another"""
        return self.__x

    @x.setter
    def x(value):
        """jum joder"""
        self.__x = value

    @property
    def y(self):
        """puff"""
        return self.__y

    @y.setter
    def y(value):
        """y setter"""
        self.__y = value
