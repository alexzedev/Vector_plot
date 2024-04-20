#Importuje bibliotekę NumPy
import numpy as np
#Importuje pyplot z biblioteki matplotlib
import matplotlib.pyplot as plt
x1 = int(input("Enter the x-axis parameter of vector 1 : "))
y1 = int(input("Enter the y-axis parameter of vector 1 : "))
x2 = int(input("Enter the x-axis parameter of vector 2 : "))
y2 = int(input("Enter the y-axis parameter of vector 2 : "))

#Tworzy wykres z odpowiednimi parametrami, wektorami na nim oraz skalą
plt.quiver([0, 0], [0, 0], [x1, x2], [y1, y2], angles='xy', scale_units='xy', scale= 1.0)
#Definiuje zakres x,y w poziomie i w pionie
plt.xlim(-20, 20)
plt.ylim(-20, 20)

#Pokazuje wykres i siatkę na nim
plt.grid()
plt.show()                  