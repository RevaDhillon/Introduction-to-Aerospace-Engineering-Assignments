#To plot the error as we change number of terms N.

#Importing packages to use required functions.
import math
import time
import sympy as sym
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

#Store exact value of integral I.
I = 0.9899352767719961

#Define a symbol and assign it to a variable.
x = sym.Symbol('x')

#Function in terms of symbols.
e = math.e
f = (e**(-x))*((sym.sin(4*x))*(sym.sin(4*x)))
#Convert to functions that can be numerically evaluated.
f = sym.lambdify(x, f)

#List initializations.
xax = []
error = []
time1 = []
#Recording the time at this instant.
start = time.time()
#Loop to get result for each N.
for i in range(1,251):
    res = 0
    #Record the number of terms N = i.
    xax.append(i)
    #Get the roots and weights for quadrature.
    roots, weights = sci.roots_legendre(i)
    #Obtain the result for I using the formula.
    for i in range(i):
        func = f(roots[i])
        res = res + func*weights[i];

    #Record the error for each N.
    error.append(abs(I - res))
    #Record the time taken to compute upto N.
    #When we are checking for a target error, we compute all values upto N.
    #Hence, this time is required(From the start).
    time1.append(time.time()-start)


#Record the log of the error values.
errorlog = np.log10(error)

#Making the plot.
plt.plot(xax, errorlog)
#Titling the plot.
plt.title("Error Variation")
#Labeling the x-axis.
plt.xlabel("Number of terms $N$ -->")
#Labeling the y-axis.
plt.ylabel("Values of log$_{10}$(error) -->")
#Setting grid properties.
plt.grid(linestyle=':')
plt.tight_layout()
#Figure saved.
plt.savefig("Log_error", dpi=300, bbox_inches="tight")
plt.show()
