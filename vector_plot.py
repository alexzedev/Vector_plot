#Importing numpy
import numpy as np
#Importing pyplot from matplotlib library
import matplotlib.pyplot as plt
x1 = int(input("Enter the x-axis parameter of vector 1 : "))
y1 = int(input("Enter the y-axis parameter of vector 1 : "))
x2 = int(input("Enter the x-axis parameter of vector 2 : "))
y2 = int(input("Enter the y-axis parameter of vector 2 : "))

#Making a plot with parameters and vectors on it with good scale
plt.quiver([0, 0], [0, 0], [x1, x2], [y1, y2], angles='xy', scale_units='xy', scale= 1.0)
#Define x,y range of the plot
plt.xlim(-20, 20)
plt.ylim(-20, 20)

#Showing plot and grid on it
plt.grid()
plt.show()                  