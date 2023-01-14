# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:46:32 2022

@author: Jérémy Archier - jeremy.archier@etu.univ-lyon1.fr

Plotting the stabilty of a Rijke Tube.

All rights reserved
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import axes3d  # Fonction pour la 3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#------------------------------Defining Function-------------------------------

def f(x,y,c1,c2,rho1,x0,L,Tau,n):
    """ Defining of complex function """
    z = x+1j*y 
    
    b1 = x0*L/c1
    b2 = (1.0-x0)*L/c2
    sol = np.cos(b2*z)*np.cos(b1*z)-1.0/2.0*np.sin(b2*z)*np.sin(b1*z)*(1.0+n*np.exp(1j*z*Tau))
    return sol

###############################################################################
################################ Main program #################################
###############################################################################

#--------------------------------Input Section---------------------------------

Nx = 10000   #max x value
Ny = 1      #max y value
Num = 100    #number of points

# Parameters
c1 = 340.0
c2 = 2*c1
rho1 = 1.2
L = 1.783
x0 = 0.2
u0 = 20.0
Tau = x0*L/u0
n = 0.01

#-------------------------PLotting the complex plane---------------------------

x = np.linspace(20,Nx, Num) #domaine de calcul en x
y = np.linspace(0,Ny, Num) #domaine de calcul en y

X, Y = np.meshgrid(x, y)

figure()

gca(projection='3d').plot_surface(X,Y,f(X,Y,c1,c2,rho1,x0,L,Tau,n), linewidth=0)
xlabel('X')
ylabel('Y')
title('3D frequency plot')

#----------------------------PLotting the contours-----------------------------

fig, ax = plt.subplots(1,1)

# plots filled contour plot
CS = ax.contourf(X, Y, f(X,Y,c1,c2,rho1,x0,L,Tau,n))
  
ax.set_title('Filled Contour frequency')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Make a colorbar for the ContourSet returned by the contourf call.
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Frequency')
  
plt.show()
