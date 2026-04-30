class Point:
    """
    A class representing a point on a plane.
    """

    def __init__(self, coords=(0, 0)):
        self.x = coords[0]
        self.y = coords[1]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def sum(self, other):
        return Point((self.x + other.x, self.y + other.y))

    def __str__(self):
        return f"({self.x}; {self.y})"

    def __repr__(self):
        return str(self)


p = Point((3, -7))
print(p)
a = Point()
print(a)
print(a.get_x())
print(p.get_y())
c = Point((-2, 4))
print(p.distance(c))
d = c.sum(p)
print(d)
print(d)
