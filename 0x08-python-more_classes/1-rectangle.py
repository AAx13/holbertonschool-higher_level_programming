#!/usr/bin/python3
'''Rectangle - defines and instance of a Rectangle requiring
2 parameters of type int (height, and width).

This module will raise TypeError if paramaters are not
of type int, and will raise ValueError if less than 0.
'''


class Rectangle():
    '''class Rectangle - Parameters(width(int), height(int))'''

    def __init__(self, width=0, height=0):
        ''' Constructor '''
        self.width = width
        self.height = height

    __width = 0
    __height = 0

    @property
    def width(self):
        ''' Getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Setter '''
        if isinstance(value, int):
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        ''' Getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Setter '''
        if isinstance(value, int):
            if value < 0:
                raise ValueError('height must be >=0')
            self.__height = value
        else:
            raise TypeError('height must be an integer')
