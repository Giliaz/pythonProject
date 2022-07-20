class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def in_circle(self, f):
        return (self.x - f.get_x()) ** 2 + (self.y - f.get_y()) ** 2 < self.radius ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

#start x, y, radius
a = Circle(0, 10, 15)
#point for find
b = Point(5, 5)
print(a.in_circle(b))
