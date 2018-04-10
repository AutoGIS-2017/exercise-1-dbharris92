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
for i in dF.itertuples():
    origPoints.append(Point(dF.from_x, dF.from_y))
    
    
    
    
    
    
    
    
    
