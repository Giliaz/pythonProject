import math


class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def __contains__(self, point):
        return (self.x - point.x) ** 2 + (self.y - point.y) ** 2 < self.radius ** 2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.height}, {self.width}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, x, y, a, b, c):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        half_perimetr = (self.a + self.b + self.c) / 2
        return half_perimetr * (half_perimetr - self.a) * (half_perimetr - self.b) * (half_perimetr - self.c) ** 0.5


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


a_circle = Circle(x=5, y=5, radius=15)
b_point = Point(x=-5, y=-5)
print(b_point in a_circle)
