class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def contains_point(self, point):
        distance = ((point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2) ** 0.5
        return distance <= self.radius
