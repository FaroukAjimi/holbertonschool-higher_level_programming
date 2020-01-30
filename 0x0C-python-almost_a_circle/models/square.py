#!/usr/bin/python3
"""Module that contains
class square
that inherits for rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square Square
    args
    Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter
        args
        size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter
        args
        self, value"""
        self.width = value
        self.height = value

    def __str__(self):
        """str
        args
        self"""
        return('[Square] ({:d}) {:d}/{:d} - {:d} '.format(self.id,
                                                          self.x,
                                                          self.y,
                                                          self.width))

    def update(self, *args, **kwargs):
        """update function
        args
        self, args, kwargs"""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
        for key, value in kwargs.items():
            if hasattr(self, key) is True:
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary
        args
        self"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
