from math import pi



class Shape:

    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == 'rectangle':
            self.height = kwargs['height']
            self.width = kwargs['width']
        elif self.shape_type == 'circle':
            self.radius = kwargs['radius']

    def calculate_area(self):
        if self.shape_type == 'rectangle':
            return self.width * self.height
        elif self.shape_type == 'circle':
            return self.radius * pi

shp = Shape('rectangle', heiht=20, width=40)
print(shp.calculate_area())

shp = Shape('rectangle', radius=20)
print(shp.calculate_area())
