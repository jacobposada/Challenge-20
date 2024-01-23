import matplotlib.pyplot as plt 
import numpy as np 

plantData = open("plants_1.csv", "r")
print (plantData) 

# graph the data to detect any initial patterns 
fig, simple_chart = plt.subplots() 
simple_chart.plot(plantData) 