#Function for computations using the midpoint method.

#Importing packages to use required functions.
from Error_plot import f
import time

#Store exact value of integral I.
I = 0.9899352767719961

#Function definition, accepts a target error.
def Mid(error):
    #Variable initializations.
    err = 100
    n=0
    #Stores the time at this instant.
    start = time.time()
    #Loop computes the integral for n segments reducing the error each time.
    while(err>error):
        n = n+1
        sum1 = 0
        #Breadth of each rectangle.
        delx = 2/n
        #Computes value of the integral.
        for i in range(0, n):
            sum1 = sum1 + delx*f((((2*i+1)/2)*delx)-1)

        #Stores the absolute error for each n.
        err = abs(I - sum1)
    #Time taken to reach a given target error recorded.
    end = time.time()
    timenet = end - start
    #Number of segments and time taken returned.
    return n, timenet



