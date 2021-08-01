import math

class Point:
    # The code copied from the previous lab.
    def __init__(self, x=0.0, y=0.0):
        # Write code here
        self.__x = x
        self.__y = y

    def getx(self):
        # Write code here
        return self.__x

    def gety(self):
        # Write code here
        return self.__y

    def distance_from_xy(self, x, y):
        # Write code here
        return math.hypot((x - self.getx()),(y - self.gety()))

    def distance_from_point(self, point):
        # Write code here
        return math.hypot((point.getx()-self.getx()),(point.gety()-self.gety()))


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        # Write code here
        self.__first_point = vertice1
        self.__second_point = vertice2
        self.__third_point = vertice3

    def perimeter(self):
        # Write code here
        self.__first_leg = self.__first_point.distance_from_point(self.__second_point)
        self.__second_leg = self.__first_point.distance_from_point(self.__third_point)
        self.__third_leg = self.__second_point.distance_from_point(self.__third_point)
        self.__leg = self.__first_leg + self.__second_leg + self.__third_leg
        return self.__leg


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
