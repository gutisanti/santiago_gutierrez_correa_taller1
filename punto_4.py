class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def perimeter(self):
        width = abs(self.point2.x - self.point1.x)
        height = abs(self.point2.y - self.point1.y)
        return 2 * (width + height)

    def area(self):
        width = abs(self.point2.x - self.point1.x)
        height = abs(self.point2.y - self.point1.y)
        return width * height

    def is_square(self):
        width = abs(self.point2.x - self.point1.x)
        height = abs(self.point2.y - self.point1.y)
        return width == height
