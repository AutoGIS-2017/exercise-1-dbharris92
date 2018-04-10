# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:12:05 2018
Auto-GIS Lesson 1, Problem 2
@author: Drew
"""

from shapely.geometry import Point, LineString, Polygon

# test point
point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)

# test line
line = LineString([point1, point2, point3])

# test poly
world_exterior = Polygon([(-180, 90), (-180, -90), (180, -90), (180, 90)])

##############
### Part 1 ###
##############
"""
Create a function called getCentroid() that takes any kind of Shapely's  
geometric -object as input and returns a centroid of that geometry. 
Demonstrate the usage of the function. 
"""
# function
def getCentroid(geometry):
    return print(geometry.centroid)
    
##############
### Part 2 ###
##############
""" 
Create a function called getArea() that takes a Shapely's Polygon -object as input and returns the area of that geometry. 
Demonstrate the usage of the function.
"""

# function
def getArea(polygon):
    return print(polygon.area)

##############
### Part 3 ###
##############
"""
Create a function called getLength() takes either a Shapely's LineString or Polygon -object as input. 
Function should check the type of the input and returns the length of the line if input is LineString and length of the exterior ring if input is Polygon. 
If something else is passed to the function, it should tell the user --> "Error: LineString or Polygon geometries required!". Demonstrate the usage of the function.
"""    

# function
def getLength(ranginess):   
    if isinstance(ranginess, LineString):
        return print(ranginess.length)
    elif isinstance(ranginess, Polygon):
        return print(ranginess.length)
    else:
        return 'Error: LineString or Polygon geometries required!'