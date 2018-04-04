# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 19:22:07 2018
Automating GIS Lesson 1
@author: harrisab2
"""

from shapely.geometry import Point, LineString, Polygon

### create point objects with coordinates
point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3d = Point(9.26, -2.456, 0.57)

### what is the type of point?
point_type = type(point1)

### get x and y coordinates
#xy = point_coords.xy
#point_coords = point1.coords
#x = point1.x
#y = point1.y

### calculate distance (gives output in Decimal Degrees by default)
point_dist = point1.distance(point2)

### create lines
line = LineString([point1, point2, point3])

### can also create a typle for same outcome
lineTuple = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

### extract coordinates from linestring (x and y coords become separate tuples)
lxy = line.xy

### find info about the line
l_length = line.length
l_centroid = line.centroid
l_buffer = line.buffer(distance=0.0001)


#####################
###### polygon ######
#####################

### make it
poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

### make it from previously create point objects
### use a loop to access coordinates from variables
poly2 = Polygon([[p.x, p.y] for p in [point1, point2, point3]])

### access geometry types as string
poly_type = poly.geom_type

### find area
p_area = poly.area

### create world polygon
world_edge = Polygon(shell=[(-180, 90), (-180, -90), (180, -90), (180, 90)]) 

### hole for the world
hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

### world without a hole
world = Polygon(shell=world_edge)

### world with a hole
world_has_hole = Polygon(shell=world, holes=hole)

### Polygon attributes and functions
world_centroid = world.centroid
world_area = world.area
world_bbox = world.bounds
world_ext = world.exterior
world_ext_length = world_ext.length 
hole_area = world_has_hole.area

######################################
######## Geometry Collections ########
######################################

# Import collections of geometric objects + bounding box
from shapely.geometry import MultiPoint, MultiLineString, MultiPolygon, box

# Create a MultiPoint object of points 1, 2, and 3
multi_point = MultiPoint([point1, point2, point3])

# Can also pass coordinate tuples inside
multi_point2 = MultiPoint([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

# Create a MultiLineString with two lines
line1 = LineString([point1, point2])
line2 = LineString([point2, point3])
multi_line = MultiLineString([line1, line2])

# Multipolygon is done in a similar manner
# Divide world into W and E hemishphere with a hole in the W
# ----------------
# Create western hemishpere exterior
west_exterior = [(-180, 90), (-180, -90), (0, -90), (0, 90)]

# Create west hole, there can be multiple holes so must list them []
west_hole = [[(-170, 80), (-170, -80), (-10, -80), (-10, 80)]]

# Create the polygon
west_poly = Polygon(shell=west_exterior, holes=west_hole)

# Create Eastern polygon using bounding box
min_x, min_y = 0, -90
max_x, max_y = 180, 90

# Create polygon using box() function
east_poly_box = box(minx=min_x, miny=min_y, maxx=max_x, maxy=max_y)

# Create our multipoly as a list []
multi_poly = MultiPolygon([west_poly, east_poly_box])