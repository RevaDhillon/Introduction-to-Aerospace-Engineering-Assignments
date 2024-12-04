#To plot the first five Legendre Polynomials.

#Importing packages to use required functions.
import math
import scipy.special as sci
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Selecting the font size and type to be used in the figure.
font={ 'family' : 'Times New Roman',
       'weight' : 'normal',
       'size' : '14'}

#Setting the selected font properties. 
matplotlib.rc('font', **font)

#Obtaining the data points for the first 5 Legendre polynomials and plotting them.
#Getting the values of x.
x = np.linspace(-1,1, 100)
#Loop for each degree of the the polynomials.
for i in range(6):
    #Generating Legendre polynomial of degree i.
    P  = sci.legendre(i)
    #Getting the values of the polynomial corresponding to each x.
    y  = P(x)
    #Plotting and labelling the Legendre polynomial for each degree i.
    plt.plot(x, y, label = "$P_" + str(i)+ "$")


#Titling the plot.
plt.title("Legendre Polynomials")
#Labeling the x-axis.
plt.xlabel("Values of x -->")
#Labeling the y-axis.
plt.ylabel("Values of $P_n$ -->")
#Setting grid properties.
plt.grid(linestyle=':')
#For three columns in the legend.
plt.legend(ncol =3)
plt.tight_layout()
#Figure saved.
plt.savefig("Leg_Poly", dpi=300, bbox_inches="tight")
plt.show()
