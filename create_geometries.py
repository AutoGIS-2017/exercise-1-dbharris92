# -*- coding: utf-8 -*-
"""
Auto-GIS Exercise 1: Working With Geometries

@author: harrisab2
"""

# import shapely packages
import shapely

# function to create a shapely point geometry object from x, y coords
def createPointGeom(x_coord, y_coord):
    return Point(x_coord, y_coord)

# Test points for below function
points = [Point(2.2, 4.2), Point(7.2, -25.1), Point(9.26, -2.456)]

# function to create shapely line object from shapley input points list
def createLineGeom(giveLine):
    if type(giveLine) is shapely.geometry.point.Point:
        return LineString(giveLine)
    else:
        return 'pointList must contain shapely point object(s)'

pls_work = createLineGeom(points)




