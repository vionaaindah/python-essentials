import math


class Point:
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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
