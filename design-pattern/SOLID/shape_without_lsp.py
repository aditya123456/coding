
class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ('width', 'height'):
            self.__dict__['width'] = value
            self.__dict__['height'] = value