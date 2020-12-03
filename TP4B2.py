from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# définition extensive d'une liste (extrait d'un tableau de mesures)
listet=[0,0.5,1,1.5,2,2.5,3,3.5,4,5,6,7,8,10,12,14,16,18,20,25,30,35,40,45,50,55]
listeC=[2,1.906,1.841,1.797,1.739,1.674,1.623,1.565,1.507,1.406,1.304,1.21,1.13,0.971,0.841,0.725,0.609,0.529,0.449,0.275,0.174,0.116,0.044,0.020,0.008,0.003]

listelnC=[]
modelelinY=[]

# calcul de la liste des logarithmes des concentrations
for val in listeC: # Pour chaque valeur de la listeC: val 
    listelnC.append(np.log(val)) # Effectuer le calcul ln(val) et ajout à la liste 

# tracé du graphique donnant ln(C) en fonction de t
plt.plot(listet,listelnC,"*",color="red")

# calcul des paramètres de la régression linéaire
(a,b,rho,_,_)=linregress(listet,listelnC)

# rho : coefficient ds corrélation linéaire
print("ln(C)=",a,"t+",b,"coef. de corr. =",rho)

for t in listet: # Pour chaque valeur du temps t de la listet
    modelelinY.append(a*t+b) # Effectuer le calcul a*t+b et ajout à la liste 

# tracé de la droite de régression linéaire
plt.plot(listet,modelelinY,color="blue")
plt.xlabel("t (en min)")
plt.ylabel("ln(c)")
plt.show()
