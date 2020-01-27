#!/usr/bin/python3


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        if type(width) != int:
            raise Exception("width must be an integer")
        if width < 0:
            raise Exception("width must be >= 0")
        if type(height) != int:
            raise Exception("height must be an integer")
        if height < 0:
            raise Exception("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise Exception("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise Exception("height must be an integer")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return ((self.__height + self.__width) * 2)
