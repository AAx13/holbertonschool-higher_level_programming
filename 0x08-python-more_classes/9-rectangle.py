#!/usr/bin/python3
'''Rectangle - defines and instance of a Rectangle requiring
2 parameters of type int (height, and width).

This module will raise TypeError if paramaters are not
of type int, and will raise ValueError if less than 0.

__str__() - Returns visual representation of a Rectangle()
based on height and width dimensions.
__repr__() - Returns string representation of the rectangle
to be able to recreate a new instance by using eval().
__del__() - Print confirmation upon successful deletion of an object.
bigger_or_equal() - Compare and return the biggest rectangle based
square() - Class method that returns a rectangle of equal width and height.
on area. Return first rectangle if they're of the same area.
area() - Returns the rectangle area.
perimeter() - Returns the rectangle perimeter.
'''


class Rectangle:
    '''This class defines a rectangle instance.'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''initialization'''
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        '''width getter'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''height getter'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''making sure the height is a positive integer'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Compare both rectangles and return the biggest based on area '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        # Compare both rectangles. Return rect_1 if both are of the same area.
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        '''to print #/'s that represent the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            rect += (str(self.print_symbol) * self.__width) + "\n"
        return (rect.rstrip())

    def __repr__(self):
        '''to stringify #/'s that represent the rectangle'''
        return ("Rectangle(%s, %s)" % (str(self.__width), str(self.__height)))

    def __del__(self):
        '''to delete the instance'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        '''returns a rectangle that is a square'''
        return (Rectangle(size, size))

    def area(self):
        '''returns the rectangle's area'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns the rectangle's perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
