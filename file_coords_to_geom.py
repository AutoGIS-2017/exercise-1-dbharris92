# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:18:37 2018
Auto GIS Lesson 1
Problem 3: Reading coordinates from a file and creating a geometries
@author: Drew
"""

import pandas as pd
from shapely.geometry import Point, LineString

#############
### Tasks ###
#############

"""
Tasks
1. Save the travelTimes_2015_Helsinki.txt into your computer.
2. Read 4 columns, i.e. 'from_x', 'from_y', 'to_x', 'to_y' from the data into Python using Pandas.
3. Create two lists called orig_points and dest_points
4. Iterate over the rows of your DataFrame and add Shapely Point -objects into the orig_points -list and dest_point -list representing the origin locations and destination locations accordingly.
"""
# Task 1-2
dF = pd.read_csv('travelTimes_2015_Helsinki.txt', sep=';', usecols=['from_x', 'from_y', 'to_x', 'to_y'])

# Task 3, create origin point and destination point lists
origPoints = []
destPoints = []

# Task 4, iterate over lists to make shapely point objects
for index, row in dF.iterrows():
    origPoints.append(Point(row['from_x'], row['from_y']))
    destPoints.append(Point(row['to_x'], row['to_y']))

#################
### Problem 4 ###   
#################
"""
1. Create a list called lines
2. Iterate over the origin and destination lists and create a Shapely LineString -object between the origin and destination point
3. Add that line into the lines -list.
4. Find out what is the average (Euclidian) distance of all the origin-destination LineStrings that we just created, and print it out.
5. To make things more reusable: write creation of the LineString and calculating the average distance into dedicated functions and use them.       
"""

# Task 1
lines= []

# Task 2/5

def makeLine(origin, destination):
    
    
    
    
    
    
    
    
    
    
    
