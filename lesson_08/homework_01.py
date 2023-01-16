"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задний ход (изменение знака скорости).
"""

class Car:
    stamp = None
    model = None
    year_of_manufacture = None
    speed = None

    def __init__(self, stamp, model, year_of_manufacture, speed):
        self.stamp, self.model, self.year_of_manufacture, self.speed = stamp, model, year_of_manufacture, speed

    def speed_plus5(self):
        self.speed += 5
        print(self.speed)

    def speed_minus5(self):
        self.speed -= 5
        print(self.speed)

    def stop(self):
        self.speed -= self.speed
        print(self.speed)

    def speed_display(self):
        print(self.speed)

    def back_draft(self):
        self.speed = 0 - self.speed









