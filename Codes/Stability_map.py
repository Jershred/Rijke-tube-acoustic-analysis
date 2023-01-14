# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:46:32 2022

@author: Jérémy Archier - jeremy.archier@etu.univ-lyon1.fr

Plotting the stabilty of a Rijke Tube.

All rights reserved
"""

import numpy as np
import matplotlib.pyplot as plt

#--------------------------------Input Section---------------------------------

tab = np.zeros(11, dtype=complex)

tab[0] = 93.5 + 1j*0.153
tab[1] = 1046.9 + 1j*0.153
tab[2] = 2000.4 + 1j*0.153
tab[3] = 2953.8 + 1j*0.152
tab[4] = 3907.3 + 1j*0.153
tab[5] = 4860.7 + 1j*0.153
tab[6] = 5814.2 + 1j*0.153
tab[7] = 6767.6 + 1j*0.152
tab[8] = 7721.1 + 1j*0.153
tab[9] = 8674.5 + 1j*0.152
tab[10] = 9628.0 + 1j*0.153

for i in range(len(tab)-1):
    plt.plot(tab[i].real,tab[i].imag, '+b')

plt.plot(tab[10].real,tab[i].imag, '+b',label="Most unstable acoustic frequencies")

plt.xlabel("Real axis",fontsize=18)
plt.ylabel("Imaginary axis",fontsize=18)
plt.title("Stability map")
plt.ylim([0, 0.2])
plt.legend()
plt.grid()
plt.show()