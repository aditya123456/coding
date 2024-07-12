from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_ared(self):
        pass


class Rectangle(Shape):

    def __init__(self, shape_type, height, width):
        super().__init__(shape_type)
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width


class Circle(Shape):

    def __init__(self, shape_type, radius):
        super().__init__(shape_type)
        self.radius = radius

    def calculate_area(self):
        return self.radius * pi

