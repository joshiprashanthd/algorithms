from typing import List, Tuple


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def absolute_distance(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    @staticmethod
    def euclidean_norm(p1, p2):
        return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

    def absolute_distance_from(self, other) -> float:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def euclidean_distance_from(self, other) -> float:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def __pow__(self, power, modulo=None):
        return Point(self.x ** power, self.y ** 2)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)