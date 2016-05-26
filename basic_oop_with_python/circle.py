import math

class Circle():

    def __init__(self, radius):
        self.__radius = radius

    def set_color(self, yellow):
        self.__color = yellow

    def get_color(self):
        return self.__color

    def set_center(self, center):
        self.__center = center

    def get_center(self):
        return self.__center

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return self.__radius * self.__radius * math.pi

    def intersection(self, c_bis):
            
