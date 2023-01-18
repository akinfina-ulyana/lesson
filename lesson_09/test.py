class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure:

    @staticmethod
    def segment_length(a: Point, b: Point):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError





