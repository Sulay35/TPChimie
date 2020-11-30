#!/usr/bin/env python
# coding: utf-8

# In[23]:


from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# définition extensive d'une liste (extrait d'un tableau de mesures)
listet=[0,0.5,1,1.5,2,2.5,3,3.5,4,5,6,7,8,10,12,14,16,18,20,25,30,35,40,45,50,55] # len = 26
listeC=1000*np.array([0.0001,0.6,0.11,0.14,0.18,0.225,0.260,0.3,0.34,0.410,0.48,0.545,0.6,0.71,0.8,0.88,0.960,1.015,1.07,1.19,1.26,1.3,1.35,1.365,1.395,1.42])
listeCMOL=[0.0001,0.6,0.11,0.14,0.18,0.225,0.260,0.3,0.34,0.410,0.48,0.545,0.6,0.71,0.8,0.88,0.960,1.015,1.07,1.19,1.26,1.3,1.35,1.365,1.395,1.42]
# Il faut mettre les valeurs de la concentration et non de l'absorbance !!

listelnC=[]
modelelinY=[]

# calcul de la liste des logarithmes des concentrations
for val in listeC:
    listelnC.append(np.log(val))

# tracé du graphique donnant ln(C) en fonction de t
plt.plot(listet,listelnC,"*",color="red")

# calcul des paramètres de la régression linéaire
(a,b,rho,_,_)=linregress(listet,listelnC)

# rho : coefficient ds corrélation linéaire
print("ln(C)=",a,"t+",b,"coef. de corr. =",rho)
for val in listet:
    modelelinY.append(a*val+b)

# tracé de la droite de régression linéaire
plt.plot(listet,modelelinY,color="blue")
plt.xlabel("t (en min)")
plt.ylabel("ln(c)")
plt.show()


# In[ ]:




