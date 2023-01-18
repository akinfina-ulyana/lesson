from lesson_09.lib_2 import Point


class Circle(Point):
    center_coord = None
    radius_length = None

    def __init__(self, center_coord, radius_length):
        self.center_coord = super().__init__(x, y)
        self.radius_length = 5

    def area_circle(self):
        s = 3.14 * (self.radius_length ** 2)
        return s

    def perimeter_circle(self):
        c = 2 * 3.14 * self.radius_length
        return c

