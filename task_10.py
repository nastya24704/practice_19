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

    def __str__(self):
        return f"({self.x}; {self.y})"

    def __repr__(self):
        return str(self)


class Segment:
    """
    A class representing a segment on a plane.
    """

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.one_intersection = self._check_one_intersection()

    def _check_one_intersection(self):
        x1, y1 = self.point1.get_x(), self.point1.get_y()
        x2, y2 = self.point2.get_x(), self.point2.get_y()

        crosses_x = (y1 > 0 and y2 < 0) or (y1 < 0 and y2 > 0)
        crosses_y = (x1 > 0 and x2 < 0) or (x1 < 0 and x2 > 0)

        return crosses_x ^ crosses_y

    def __str__(self):
        return f"({self.point1}, {self.point2})"

    def __repr__(self):
        return str(self)


class CoordinateSystem:
    """
    A class representing a coordinate system with segments.
    """

    def __init__(self):
        self.segments = []

    def add_segment(self, segment):
        """Add a segment to the coordinate system."""
        self.segments.append(segment)

    def axis_intersection(self):
        """
        Return the number of segments that intersect exactly one axis.
        """
        count = 0
        for segment in self.segments:
            if segment.one_intersection:
                count += 1
        return count

    def __str__(self):
        return str(self.segments)

    def __repr__(self):
        return str(self)

p1 = Point((-2, 7))
print(p1)
p2 = Point((3, 4))
s1 = Segment(p1, p2)
print(s1)
print(s1.one_intersection)
xy = CoordinateSystem()
xy.add_segment(s1)
p3 = Point((2, -8))
p4 = Point((4, 16))
s2 = Segment(p3, p4)
xy.add_segment(s2)
xy.add_segment(Segment(p4, p2))
xy.add_segment(Segment(Point((-5, 3)), Point((-13, -6))))
print(xy.segments)
print(xy)
print(xy.axis_intersection())
