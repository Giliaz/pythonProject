class Circle:
    def __init__(self, x=0, y=0, radius=10):
        self.x = x
        self.y = y
        self.radius = radius
        print(self.x, self.y, self.radius)

    def in_circle(self, f):
        print(f.x,  f.y)
        return (self.x - f.get_x()) ** 2 + (self.y - f.get_y()) ** 2 < self.radius ** 2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

#circle x, y, radius
a = Circle(x=5, y=5, radius=15)
#point x, y
b = Point(x=-5, y=-5)

print(a.in_circle(b))
