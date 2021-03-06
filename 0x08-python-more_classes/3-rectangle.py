#!/usr/bin/python3


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        return (str(self.__height * self.__width))

    def perimeter(self):
        return (str(self.__height + self.__width) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ('')
        rect = []

        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
