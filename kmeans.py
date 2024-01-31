import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import random 

open_file = open("plants_1.csv", "r")
list_file = list(open_file)
complete_data = [i.split(",") for i in list_file[1:]] 

# print (plantData) 

# isolate each variable of the plant data into its own list 
for plant in complete_data: 
    id = [int(entry[0]) for entry in complete_data] 
    sepal_width = [float(entry[1]) for entry in complete_data]
    sepal_length = [float(entry[2]) for entry in complete_data] 
    petal_width = [float(entry[3]) for entry in complete_data] 
    petal_length = [float(entry[4]) for entry in complete_data]

# check the data is formatted correctly 
# print (sepal_length) 

# graph the data to detect any initial patterns 
simple_chart = plt.scatter(petal_length, sepal_length) 
# plt.show() 

# create list of tuples with data 
plant_data = zip(id, petal_length, sepal_length) 

# range of variables 
petal_range = (min(petal_length), max(petal_length)) 
sepal_range = (min(sepal_length), max(sepal_length)) 

class Centroid: 

    def __init__(self, name): 
        self.name = name 

        # assign random floats within the range, round to 2 decimals 
        self.petal_length = round(random.uniform(min(petal_length), max(petal_length)), 2) 
        self.sepal_length = round(random.uniform(min(sepal_length), max(sepal_length)), 2) 
    
    def __str__(self): 
        return (f"Centroid {self.name} has a petal length {self.petal_length} and a sepal length {self.sepal_length}") 
    

class Point: 

    def __init__(self, id, petal_length, sepal_length): 
        self.id = id 
        self.petal_length = petal_length 
        self.sepal_length = sepal_length 

    # identify which centroid is closest 
    def closest_dist(self, centroids): 
        dist = []
        for centroid in centroids: 
            #dist_from_centroid = np.sqrt
            petal_len = (self.petal_length - centroid.petal_length)**2 
            sepal_len = (self.sepal_length - centroid.sepal_length)**2 
            dist_from_centroid = np.sqrt(petal_len + sepal_len) 
            dist.append(dist_from_centroid) 
        # the index will signify which centroid is closest 
        return dist.index(min(dist)) 
    
    def __str__(self): 
        return f"Point {self.id} has petal length {self.petal_length} and sepal length {self.sepal_length}"
    

## start with two random centroids 

# list of centroids 
centroids = [] 

# appending centroids to list 
centroids.append(Centroid('A')) 
centroids.append(Centroid('B')) 

## determine which centroid is closest to each point 

# create points 
points = [] 
for plant in plant_data: 
    points.append(Point(plant[0], plant[1], plant[2])) 

# append the points to different lists based on the centroid (using identifier) 
sorted_points = [[] for entry in range(len(centroids))]
for point in points: 
   index = point.closest_dist(centroids) 
   sorted_points[index].append(point.id)

print (sorted_points[0]) 
# change centroid to the average of the points' features 
# repeat until no changes happen in the list 