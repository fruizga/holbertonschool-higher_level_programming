#!/usr/bin/python3
"""class Rectangle inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Private instance att __width,  __height, __x and __y a class constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of the class private instances
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """receive value as parameter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """receive value as parameter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """receives value as parameter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """Receive value as parameter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area
        """
        return (self.__width * self.__height)

    def display(self):
        """Print in stdout the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.__y)]
        for row in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for Column in range(self.__width)]
            print("")

    def __str__(self):
        """[Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.width = j
                if i == 2:
                    self.height = j
                if i == 3:
                    self.x = j
                if i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Dictionary as representation of a rectangle
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
