#!/usr/bin/python3
'''Square class.
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class.'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        return string representation of square
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Return size (width)
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """Sets value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign values and attributes
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Dictionary representation of a square
        """
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
