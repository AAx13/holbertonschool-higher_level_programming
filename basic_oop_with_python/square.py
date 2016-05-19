import math

class Square():
    def __init__(self, side_length):
        self.__side_length = side_length

    def set_center(self, center):
        self.__center = [0, 0]

    def get_center(self):
        return self.__center

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_side_length(self, side_length):
        self.__side_length = side_length

    def get_side_length(self):
        return self.__side_length

    def area(self):
        return self.__side_length * self.__side_length

    def print_square(self):

        size = self.__side_length
        inner = size - 2
        print('*' * size)
        for i in range(inner):
            print('*' + ' ' * inner + '*')
        print('*' * size)
