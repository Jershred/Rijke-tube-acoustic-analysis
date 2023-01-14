# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 08:52:01 2022

@author: Jérémy Archier - jeremy.archier@etu.univ-lyon1.fr

Newton-Raphson method to find the frequencies of a Rijke Tube. 

Paramètres:
    
    - c1 : speed of sound in first part
    - c2 : speed of sound in second part
    - rho1 : air density in the first part of the tube
    - x0 : provides the position of the flame
    - L : length of the tube
    - Tau : la condition de vitesse initiale
    - n : normalized flame response
    - uO : mean speed of the flow

All rights reserved
"""

import numpy as np

#------------------------------Defining Function-------------------------------

def f(x,c1,c2,rho1,x0,L,Tau,n):
    """ Defining of function """
    
    b1 = x0*L/c1
    b2 = (1.0-x0)*L/c2
    sol = np.cos(b2*x)*np.cos(b1*x)-1.0/2.0*np.sin(b2*x)*np.sin(b1*x)*(1.0+n*np.exp(1j*x*Tau))
    return sol

def g(x,c1,c2,rho1,x0,L,Tau,n):
    """ Defining derivative of function """
    
    b1 = x0*L/c1
    b2 = (1.0-x0)*L/c2
    A = -b2*np.sin(b2*x)*np.cos(b1*x)-b1*np.cos(b2*x)*np.sin(b1*x)
    B = -1.0/2.0*(b2*np.cos(b2*x)*np.sin(b1*x)+b1*np.sin(b2*x)*np.cos(b1*x))*(1.0+n*np.exp(1j*x*Tau))
    C = -1.0/2.0*np.sin(b2*x)*np.sin(b1*x)*(1.0+1j*n*Tau*np.exp(1j*x*Tau))
    sol = A + B + C
    return sol

def newtonRaphson(x_guess,e,N,c1,c2,rho1,x0,L,Tau,n):
    """
    Implementation of the algorithm
    Parameters
    ----------
    x_guess : guess value of function zeros.
    e : error
    N : max number iteration 

    Returns
    -------
    x1 : the angular frequency 

    """
    #print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x_guess,c1,c2,rho1,x0,L,Tau,n) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x_guess - f(x_guess,c1,c2,rho1,x0,L,Tau,n)/g(x_guess,c1,c2,rho1,x0,L,Tau,n)
        freq = x1/(2*np.pi)
        #print('Iteration-%d, x1 = %0.3f and f(x1) = %0.3f' % (step, x1, f(x1,c1,c2,rho1,x0,L,Tau,n)))
        x_guess = x1
        step = step + 1
        
        if step > N: #we limit the maximum number of iterations if it diverges
            flag = 0
            break
        
        condition = abs(f(x1,c1,c2,rho1,x0,L,Tau,n)) > e #test the distance
    
    if flag==1:
        freq = x1/(2*np.pi)
        #print('\nRequired root is: %0.8f' % freq)
        #print('({0.real:.2f} + {0.imag:.2f}i)'.format(freq))
    else:
        print('\nNot Convergent.')
    
    return (freq)

###############################################################################
################################ Main program #################################
###############################################################################

#--------------------------------Input Section---------------------------------

e = 10e-5   #error tolerated for frequencies
N = 10e6   #maximum number of iterations

# Parameters
c1 = 340.0
c2 = 2*c1
rho1 = 1.2
L = 1.783
x0 = 0.2
u0 = 20.0
Tau = x0*L/u0
n = 0.01

#-----------------------Starting Newton Raphson Method-------------------------

#Loop parameters 
N_min = 1            #minimum value of the loop
N_max = int(1e5)    #maximul value of the loop
step = 100          #step of the loop between iterations

freq = []            #complex table stocking all the frequencies

#Loop to find every frequency linked to unstable acoustic modes
for i in range(N_min,N_max,step):
    omega_guess = float(i) + 0j #convert the guess to complex
    frequence = newtonRaphson(omega_guess,e,N,c1,c2,rho1,x0,L,Tau,n)
    
    if frequence.imag > 0.0 : #we add the unstable frequency
        freq.append(frequence)
        
#----------------------Re-arangement of the frequencies------------------------

freq_sorted_real = [] #table stocking the non zeros frequencies
freq_sorted_imag = [] #table stocking the non zeros frequencies
      
for i in range(len(freq)):
    if freq[i].real > 0.0 and freq[i].imag > 1.0e-1: #For none zeros positive values we put them in an other table
        if freq[i].real <= 10000.0 and freq[i].real >= 10.0:
            freq_sorted_real.append(freq[i].real)
            freq_sorted_imag.append(freq[i].imag)

for i in range(len(freq_sorted_real)):
    freq_sorted_real[i] = round(freq_sorted_real[i], 1) #We round the frequencies to sort remove the duplicates more easily
    freq_sorted_imag[i] = round(freq_sorted_imag[i], 3) #We round the frequencies to sort remove the duplicates more easily

freq_sorted_real = list(set(freq_sorted_real)) #remove all the same values
freq_sorted_imag = list(set(freq_sorted_imag)) #remove all the same values

freq_sorted_real.sort() #sort the table in ascending order