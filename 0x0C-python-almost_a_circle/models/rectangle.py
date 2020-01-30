#!/usr/bin/python3
"""module that will contains Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Base class
    args
    Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter
        arg
        self"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

    @property
    def height(self):
        """height getter
        args
        self"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        args
        self
        value"""
        self.__height = value
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

    @property
    def x(self):
        """x getter
        args
        self"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        args
        self
        value"""
        self.__x = value
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

    @property
    def y(self):
        """y getter
        args
        self"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        args
        self
        value"""
        self.__y = value
        if(type(value) is not int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

    def area(self):
        """area function
        args
        self"""
        return (self.width * self.height)

    def display(self):
        """display function
        args
        self"""
        for z in range(self.y):
            print()
        for i in range(self.height):
            for w in range(self.x):
                print(' ', end="")
            for y in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """str function
        args
        self"""
        return('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height))

    def update(self, *args, **kwargs):
        """update function
        args
        self
        args
        kwargs"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
        for key, value in kwargs.items():
            if hasattr(self, key) is True:
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary
        args
        self"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
