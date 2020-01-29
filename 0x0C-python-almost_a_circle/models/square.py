#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return('[Square] ({:d}) {:d}/{:d} - {:d} '.format(self.id, self.x, self.y, self.width))

    def to_dictionary(self):
        return {'id' : self.id, 'size' : self.size, 'x' : self.x, 'y' : self.y}
