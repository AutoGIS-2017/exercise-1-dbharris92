# -*- coding: utf-8 -*-
"""
Auto-GIS Exercise 1: Working With Geometries

@author: harrisab2
"""

# import shapely packages
from shapely.geometry import Point, MultiPoint, LineString, Polygon


# function to create a shapely point geometry object from x, y coords
def createPointGeom(x_coord, y_coord):
    return Point(x_coord, y_coord)

# function to create shapely line object from shapley input points list
# sample vertices 
vertices = [Point(2.2, 4.2), Point(7.2, -25.1), Point(9.26, -2.456)]

# function 
def createLineGeom(points):
    if all(isinstance(x, Point) for x in points):
       return LineString(points)
    else:
        return 'pointList must contain shapely point object(s)'
my_Line = createLineGeom(vertices)
print(my_Line)

# function to take list of coordinate tuples or shapely points and return 
# input points and coords
point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)

point_coords = ((point1.coords), (point2.coords), (point3.coords)) 

# function 
def createPolyGeom(givePoly):
    for x in givePoly:
        return Polygon([[p.x, p.y] for p in givePoly])
    else:
        return 'givePoly must contain point objects or point tuples'



 
