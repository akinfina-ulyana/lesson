class Car:
    stamp = None
    model = None
    year_of_manufacture = None
    speed = None

    def __init__(self, stamp, model, year_of_manufacture, speed = 0):
        self.stamp, self.model, self.year_of_manufacture, self.speed = stamp, model, year_of_manufacture, speed

    def speed_plus5(self):
        self.speed = self.speed + 5
        return self.speed

    def speed_minus5(self):
        return self.speed - 5

    def stop(self):
        return 0

    def speed_display(self):
        print(self.speed)

    def back_draft(self):
        return 0 - self.speed





