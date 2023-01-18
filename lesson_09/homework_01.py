"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса; методы:
нахождение периметра и площади окружности), Triangle (атрибуты: три точки, методы: нахождение
площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""

from lesson_09.lib_2 import Point


class Triangle(Point):
    coord_1 = None
    coord_2 = None
    coord_3 = None

    def __init__(self, coord_1, coord_2, coord_3):
        self.coord_1 = super().__init__(x, y)
        self.coord_2 = super().__init__(x, y)
        self.coord_3 = super().__init__(x, y)


    def area_triangl(self):
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        p = (a + b + c)
        a = ((x2 - x1) + (y2 - y1)) ** 0.5
        b = ((x3 - x2) + (y3 - y3)) ** 0.5
        c = ((x3 - x1) + (y3 - y1)) ** 0.5
        return s

    def perimetr_triangl(self):
        perimetr = a + b + c
        return perimetr


