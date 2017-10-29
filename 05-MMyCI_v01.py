# -*- coding: utf-8 -*-
"""
Autor: Becerra Pedraza Daniel
Ejercicio 6 de Tarea
Modelación Matemática y Computacional de Sistemas Terrestres I
Posgrado en Ciencias de la Tierra, Instituto de Geofísica, UNAM
Dres. Ismael Herrera Revilla, Guillermo Hernández García 
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def p1(x1,x2,x3,t):
   return 3*t**2/2

def p2(x1,x2,x3,t):
   return -np.cos(2*t)/2

def p3(x1,x2,x3,t):
   return x3*t

n=0.001
T= np.arange(0,1+n,n)
x = np.array([1,1,0])
p_1 = p1(x[0],x[1],x[2],T)
p_2 = p2(x[0],x[1],x[2],T)
p_3 = p3(x[0],x[1],x[2],T)

################
# First subplot
################

# Twice as tall as it is wide.
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(2, 2, 1)
l1 = ax.plot(T,p_1,"-", color="blue")
ax.grid(True)
ax.set_ylabel('$p_{1}$')
ax.set_xlabel('$t$')


################
# Second subplot
################

# Twice as tall as it is wide.
ax = fig.add_subplot(2, 2, 2)
l2 = ax.plot(T,p_2,"-", color="green")
ax.grid(True)
ax.set_ylabel('$p_{2}$')
ax.set_xlabel('$t$')

################
# Third subplot
################

# Twice as tall as it is wide.
ax = fig.add_subplot(2, 2, 3)
l3 = ax.plot(T,p_3,"-", color="red")
ax.grid(True)
ax.set_ylabel('$p_{3}$')
ax.set_xlabel('$t$')

#################
# Fourth subplot
#################
ax = fig.add_subplot(2, 2, 4, projection='3d')
c = T
sc1 = ax.scatter(p_2, p_3, p_1, c=c, vmin=0, vmax=1, s=5)
ax.view_init(elev=20, azim=235)
ax.set_xlabel('$p_{1}$')
ax.set_ylabel('$p_{2}$')
ax.set_zlabel('$p_{3}$')
plt.colorbar(sc1)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()

#################
# Sixth subplot
#################
ax = fig.add_subplot(2, 2, 4, projection='3d')
c = T
sc1 = ax.scatter(p_2, p_3, p_1, c=c, vmin=0, vmax=1, s=5)
ax.view_init(elev=20, azim=235)
ax.set_xlabel('$p_{1}$')
ax.set_ylabel('$p_{2}$')
ax.set_zlabel('$p_{3}$')
plt.colorbar(sc1)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()
