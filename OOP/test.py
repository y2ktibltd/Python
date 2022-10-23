#!/usr/bin/env python3
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x=x
        self.__y=y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
    
    def distance_from_xy(self, x, y):
        xl=self.__x - x
        yl=self.__y - y
        return math.hypot(xl,yl)

    def distance_from_point(self, point):
        xl=self.__x - point.getx()
        yl=self.__y - point.gety()
        return math.hypot(xl,yl)

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices=[vertice1,vertice2,vertice3]

    def perimeter(self):
        per=0
        for i in range(len(self.__vertices)):
            per+=self.__vertices[i].distance_from_point(self.__vertices[(i+1)%3])
        return per

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

