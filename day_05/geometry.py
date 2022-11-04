from math import copysign


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    @classmethod
    def from_coor(cls, x1, y1, x2, y2):
        return cls(Point(x1, y1), Point(x2, y2))

    def is_horizontal(self):
        return self.point_1.x == self.point_2.x

    def is_vertical(self):
        return self.point_1.y == self.point_2.y

    def is_diagonal(self):
        return abs(self.point_1.x - self.point_2.x) == abs(self.point_1.y - self.point_2.y)

    def get_points_hor_ver(self):
        points = []
        for x in range(min(self.point_1.x, self.point_2.x), max(self.point_1.x, self.point_2.x) + 1):
            for y in range(min(self.point_1.y, self.point_2.y), max(self.point_1.y, self.point_2.y) + 1):
                points.append(Point(x, y))

        return points

    def get_points_diag(self):
        points = []
        delta = abs(self.point_1.x - self.point_2.x)
        dir_x = copysign(1, self.point_2.x - self.point_1.x)
        dir_y = copysign(1, self.point_2.y - self.point_1.y)
        for i in range(0, delta + 1):
            points.append(Point(self.point_1.x + dir_x * i, self.point_1.y + dir_y * i))

        return points


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x + self.y)
