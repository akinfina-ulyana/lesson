"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса; методы:
нахождение периметра и площади окружности), Triangle (атрибуты: три точки, методы: нахождение
площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""

from lesson_09.lib_2 import Point


class Triangle:

    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def area_triangl(self):
        a = ((self.x2 - self.x1) + (self.y2 - self.y1)) ** 0.5
        b = ((self.x3 - self.x2) + (self.y3 - self.y3)) ** 0.5
        c = ((self.x3 - self.x1) + (self.y3 - self.y1)) ** 0.5

        p = (a + b + c)/2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(s)
        return s

    def perimetr_triangl(self):
        a = ((abs(self.x2 - self.x1)) + (abs(self.y2 - self.y1))) ** 0.5
        b = ((abs(self.x3 - self.x2)) + (abs(self.y3 - self.y3))) ** 0.5
        c = ((abs(self.x3 - self.x1)) + (abs(self.y3 - self.y1))) ** 0.5

        perimetr = a + b + c
        perimetr = print(float(perimetr))

        return a

triangle = Triangle(3, 6, 11, 3, 8, 4)
triangle.perimetr_triangl()

