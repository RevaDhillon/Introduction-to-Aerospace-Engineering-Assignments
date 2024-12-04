#To obtain the number of terms and time taken for a target error.

#Importing packages to use required functions.
from Error_plot import error
from Error_plot import xax
from Error_plot import time1
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from Midpoint import Mid 


#Selecting the font size and type to be used in the figure.
font={ 'family' : 'Times New Roman',
       'weight' : 'normal',
       'size' : '14'}

#Setting the selected font properties. 
matplotlib.rc('font', **font)

#Variable initializations.
target_error = []
N = []
T = []

#Storing the target errors.
for j in range(1,16):
    target_error.append(10**(-j))


#Starting a loop for each target error.
for j in range(15):
    #Starting a loop for each N in the Gauss-Legendre quadrature.
    for i in range(248):
        #Condition for error.
        if (error[i+1]<=target_error[j] and error[i]>= target_error[j]):
            #Recording the number of terms needed.
            N.append(xax[i])
            #Recording the computational time.
            T.append(time1[i])
            break

#Midpoint method is "best".
#Variable initializations.
N_1 = []
T_1 = []
target_error1 = []
#Starting a loop for each target error.
for i in range(7):
    #Recording the number of terms needed and computational time.
    num, timenet = Mid(target_error[i])
    N_1.append(num)
    T_1.append(timenet)
    target_error1.append(target_error[i])


#Conversion to log scale.
target_error = np.log10(target_error)
target_error1 = np.log10(target_error1)

#Making the number of terms plot.
plt.plot(target_error, np.log10(N), label = "Gaussian Quadrature")
plt.plot(target_error1, np.log10(N_1), label = "Midpoint Method")
#Titling the plot.
plt.title("Target Error")
#Labeling the x-axis.
plt.xlabel("Values of log$_{10}$(Target error) -->")
#Labeling the y-axis.
plt.ylabel("Number of terms required $N$ (Log scale) -->")
#Setting grid properties.
plt.grid(linestyle=':')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("Target_error_N", dpi=300, bbox_inches="tight")
plt.show()

#Making the computational time plot.
plt.plot(target_error, np.log10(T), label = "Gaussian Quadrature")
plt.plot(target_error1, np.log10(T_1), label = "Midpoint Method")
#Titling the plot.
plt.title("Target Error")
#Labeling the x-axis.
plt.xlabel("Values of log$_{10}$(Target error) -->")
#Labeling the y-axis.
plt.ylabel("Time required(seconds) (Log scale) -->")
#Setting grid properties.
plt.grid(linestyle=':')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("Target_error_T", dpi=300, bbox_inches="tight")
plt.show()
