#!/usr/bin/python3
''' class Rectangle - with parameters width(int) and height(int) '''


class Rectangle():

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    __width = 0
    __height = 0

    # width getter
    @property
    def width(self):
        return self.__width

    # width setter
    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        else:
            raise TypeError('width must be an integer')

    # height getter
    @property
    def height(self):
        return self.__height

    # height setter
    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError('height must be >=0')
            self.__height = value
        else:
            raise TypeError('height must be an integer')
