import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import random

open_file = open("plants_1.csv", "r")
list_file = list(open_file)
complete_data = [i.split(",") for i in list_file[1:]] 

# test the data format 
# print (plantData) 

# isolate each variable of the plant data into its own list, check the format 
for plant in complete_data: 
    id = [int(entry[0]) for entry in complete_data] 
    sepal_length = [float(entry[2]) for entry in complete_data] 
    petal_length = [float(entry[4]) for entry in complete_data]

# print (sepal_length) 

# graph the data to detect any initial patterns 
simple_chart = plt.scatter(petal_length, sepal_length) 
# plt.show() 

# create list of lists with relevant data, check the format 
plant_data = [[x,y,z] for x,y,z in zip(id, sepal_length, petal_length)]

# print (plant_data) 

class KMeans: 
    def __init__(self, k=3, max_iters=100): 
        self.k = k 
        self.max_iters = max_iters 

    # calculate the closest centroid to point 
    def closest_dist(self, point, centroids): 
        dist = []
        for centroid in centroids: 
            #dist_from_centroid = np.sqrt
            petal_len = (point[1] - centroid[0])**2 
            sepal_len = (point[2] - centroid[1])**2 
            dist_from_centroid = np.sqrt(petal_len + sepal_len) 
            dist.append(dist_from_centroid) 
        # the index will signify which centroid is closest 
        return dist.index(min(dist)) 

    def fit(self, dataset): 
        self.centroids = [] 

        # Initialize k centroids by randomly selecting k points from the dataset 
        random_indices = random.sample(range(len(dataset)), self.k)
        random_points = [dataset[i][1:] for i in random_indices]
        self.centroids = [random_points[i] for i in range(self.k)] 
        print(self.centroids) 

        # Iterate at most max_iters times 
        for i in range(self.max_iters): 
            centroid_assignments = {} 

            for k in range(self.k): 
                centroid_assignments[k] = [] 

            # Assign data points to nearest centroid 
            for point in dataset: 
                assigned_centroid = self.closest_dist(point, self.centroids) 
                centroid_assignments[assigned_centroid].append(point) 
            
            # Store current centroids as previous for the next iteration 
            prev_centroids = self.centroids 

            # Update centroids 
            for assignment in centroid_assignments: 
                # print(centroid_assignments[assignment]) 

                # Find average values of clusters 
                cluster_petal_lengths = [sublist[1] for sublist in centroid_assignments[assignment]] 
                avg_p_length = sum(cluster_petal_lengths) / len(cluster_petal_lengths) 
                cluster_sepal_lengths = [sublist[2] for sublist in centroid_assignments[assignment]] 
                avg_s_length = sum(cluster_sepal_lengths) / len(cluster_sepal_lengths) 
                
                # Assign new values to centroids 
                self.centroids[assignment] = [avg_p_length, avg_s_length] 

            # Check if centroids have converged 
            optimized = True 
            for c in range(self.k): 
                original_centroid = prev_centroids[c] 
                current_centroid = self.centroids[c] 

                # Calculate their change 
                relative_change = [ 
                    ((current_centroid[0] - original_centroid[0]) / original_centroid[0]) * 100.0, 
                    ((current_centroid[1] - original_centroid[1]) / original_centroid[1]) * 100.0
                ]

                # Check if relative change is above threshold 
                if sum(relative_change) > 0.01: 
                    optimized = False 
                    break 
            if optimized: 
                break 
            
        print (self.centroids)        

# Create KMeans object to utilize dataset in 
plant_kmeans = KMeans() 

# Optimize the centroids based on the plant data 
plant_kmeans.fit(plant_data) 