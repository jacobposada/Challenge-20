import matplotlib.pyplot as plt 
import numpy as np 

openFile = open("plants_1.csv", "r")
listFile = list(openFile)
plantData = [i.split(",") for i in listFile[1:]] 

# print (plantData) 

# isolate each variable of the plant data into its own list 
for plant in plantData: 
    identifier = [int(entry[0]) for entry in plantData] 
    sepal_width = [float(entry[1]) for entry in plantData]
    sepal_length = [float(entry[2]) for entry in plantData] 
    petal_width = [float(entry[3]) for entry in plantData] 
    petal_length = [float(entry[4]) for entry in plantData]

# check the data is formatted correctly 
print (sepal_length) 

# graph the data to detect any initial patterns 
simple_chart = plt.scatter(sepal_length, petal_length) 
plt.show() 

