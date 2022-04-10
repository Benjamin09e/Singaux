# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:36:33 2022

@author: Benjamin EKIA
"""
# import de la bibliothèque numpy en lui donnant le surnom np 
import numpy as np

# import de la bibliothèque matplolib en lui donnant le surnom plt
import matplotlib.pyplot as plt

# taille de la figure
fig = plt.figure(figsize=(10,7))

# definition du signal de vibation 

M = 3
F = 65
T = 10
fe = 5000


t = np.arange(T)/fe
x1 = 0.5 


# génération du signal x(t)
x = x1*np.cos(2*np.pi*M*F*t)

# affichage 
plt.legend(loc ='upper right')
plt.plot(t, x, "b-")
plt.title("Signaux d'engrenages")
plt.xlabel("temps (t)")
plt.ylabel("fréquences (f)")
plt.grid(True)
plt.show()







 



