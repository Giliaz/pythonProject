class Circle:
    def __init__(self, x=0, y=0, radius=10):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        return (self.x - point.x) ** 2 + (self.y - point.y) ** 2 < self.radius ** 2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


circle = Circle(x=5, y=5, radius=15)
point = Point(x=-5, y=-5)
print(circle.contains(point))
