#!/usr/bin/python3
"""Rectangle
"""

Base = __import__('base').Base
"""Inherits from base
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
                
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(value):
        self.__width = value
    
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(value):
        self.height = value
    
    @property
    def x(self):
        return self.x
    
    @x.setter
    def x(value):
        self.x = value
    
    @property
    def y(self):
        return self.y
    
    @y.setter
    def y(value):
        self.y = value

        