#Root finding methods.

#Importing packages to use required functions.
import time
import math
import sympy as sym
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Selecting the font size and type to be used in the figure.
font={ 'family' : 'Times New Roman',
       'weight' : 'normal',
       'size' : '14'}

#Setting the selected font properties. 
matplotlib.rc('font', **font)

#Function for Bisection Method
def Bisection_method(f, a, b, tol):
    #Set maximum number of iterations.
    n_max = 10000000
    #Store the value of the function for each iteration.
    #Each value is supposed to be a better approximation to the root.
    y=[f(a)]
    #List to store time.
    WCtime = [0]
    #Store the current time since epoch.
    start = time.time()
    #Loop for bisection method.
    for i in range(n_max):
        #Compute intermediate value.
        c = (a+b)/2
        #Add function value to the list.
        y.append(f(c))
        #Add time since the start of computations to the list.
        WCtime.append(time.time() - start)
        #Check for root.
        if abs(f(c))<tol:
            return c, i+1, y, WCtime
        #Check for signs of functions
        elif f(c)*f(a)<0:
            b = c
        else:
            a=c
    #If no root is found, return None.
    return None, n_max, y, WCtime

#Function for Newton Method
def Newton_method(f, df, x0, tol):
    #Set maximum number of iterations.
    n_max = 10000000
    #Store the value of the function for each iteration.
    y = [f(x0)]
    #List to store time.
    WCtime = [0]
    #Store the current time since epoch.
    start = time.time()
    #Loop for newton method.
    for i in range(n_max):
        #Compute the next better approximation using the formula.
        x1 = x0 - (f(x0)/df(x0))
        #Add function value to the list.
        y.append(f(x1))
        #Add time since the start of computations to the list.
        WCtime.append(time.time() - start)
        #Check for root.
        if abs(f(x1))<tol:
            return x1, i+1, y, WCtime
        else:
            x0 = x1
    #If no root is found, return None.
    return None, n_max, y, WCtime

#Function for Secant Method
def Secant_method(f, x1, x0, tol):
    #Set maximum number of iterations.
    n_max = 10000000
    #Store the value of the function for each iteration.
    y = [f(x1)]
    #List to store time.
    WCtime = [0]
    #Store the current time since epoch.
    start = time.time()
    #Loop for secant method.
    for i in range(n_max):
        #Compute the next better approximation using the formula.
        x2 = x1 - (f(x1)*(x1 - x0))/(f(x1) - f(x0))
        #Add function value to the list.
        y.append(f(x2))
        #Add time since the start of computations to the list.
        WCtime.append(time.time() - start)
        #Check for root.
        if abs(f(x2))<tol:
            return x2, i+1, y, WCtime
        else:
            x0 = x1
            x1 = x2
    #If no root is found, return None.
    return None, n_max, y, WCtime
        
#Define a symbol and assign it to a variable.
x = sym.Symbol('x')

#Function in terms of symbols.
f1 = x**3 - 3*x*x - x - 9
#Derivative in terms of symbols.
df1 = f1.diff(x)
#Convert to functions that can be numerically evaluated.
f1 = sym.lambdify(x, f1)
df1 = sym.lambdify(x, df1)

#Function in terms of symbols.
e = math.exp(1)
f2 = (e**x)*(x**3 - 3*x*x - x - 9)
#Derivative in terms of symbols.
df2 = f2.diff(x)
#Convert to functions that can be numerically evaluated.
f2 = sym.lambdify(x, f2)
df2 = sym.lambdify(x, df2)

#Function in terms of symbols.
f3 = x**3 - 2*x + 2
#Derivative in terms of symbols.
df3 = f3.diff(x)
#Convert to functions that can be numerically evaluated.
f3 = sym.lambdify(x, f3)
df3 = sym.lambdify(x, df3)

#Starting sets.
set1 = [3.5, 4]
set2 = [3.6, 5.1]

#Evaluating f1 using set1 by all 3 methods.
BMset1_rootf1, BMset1_iterf1, BMset1_f1x, BMset1_timef1 = Bisection_method(f1, set1[0], set1[1], 10**(-6))
NMset1_rootf1, NMset1_iterf1, NMset1_f1x, NMset1_timef1 = Newton_method(f1, df1, set1[0], 10**(-6))
SMset1_rootf1, SMset1_iterf1, SMset1_f1x, SMset1_timef1 = Secant_method(f1, set1[0], set1[1], 10**(-6))
#Evaluating f1 using set2 by all 3 methods.
BMset2_rootf1, BMset2_iterf1, BMset2_f1x, BMset2_timef1 = Bisection_method(f1, set2[0], set2[1], 10**(-6))
NMset2_rootf1, NMset2_iterf1, NMset2_f1x, NMset2_timef1 = Newton_method(f1, df1, set2[0], 10**(-6))
SMset2_rootf1, SMset2_iterf1, SMset2_f1x, SMset2_timef1 = Secant_method(f1, set2[0], set2[1], 10**(-6))

#Evaluating f2 using set1 by all 3 methods.
BMset1_rootf2, BMset1_iterf2, BMset1_f2x, BMset1_timef2 = Bisection_method(f2, set1[0], set1[1], 10**(-6))
NMset1_rootf2, NMset1_iterf2, NMset1_f2x, NMset1_timef2 = Newton_method(f2, df2, set1[0], 10**(-6))
SMset1_rootf2, SMset1_iterf2, SMset1_f2x, SMset1_timef2 = Secant_method(f2, set1[0], set1[1], 10**(-6))
#Evaluating f2 using set2 by all 3 methods.
BMset2_rootf2, BMset2_iterf2, BMset2_f2x, BMset2_timef2 = Bisection_method(f2, set2[0], set2[1], 10**(-6))
NMset2_rootf2, NMset2_iterf2, NMset2_f2x, NMset2_timef2 = Newton_method(f2, df2, set2[0], 10**(-6))
SMset2_rootf2, SMset2_iterf2, SMset2_f2x, SMset2_timef2 = Secant_method(f2, set2[0], set2[1], 10**(-6))

#Plotting f1(x) against number of iterations for both starting sets, using all 3 methods.
plt.plot(range(0, BMset1_iterf1+1), BMset1_f1x, ":r", label = "Set1 Bisection Method")
plt.plot(range(0, BMset2_iterf1+1),BMset2_f1x, "--b", label = "Set2 Bisection Method")
plt.title("f1(x) against Number of Iterations")
#Labeling the x-axis.
plt.xlabel("Number of Iterations -->")
#Labeling the y-axis.
plt.ylabel("Values of f1(x) -->")
#Setting grid properties.
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f1_iterationsBM", dpi=300, bbox_inches="tight")
plt.show()

plt.plot(range(0, NMset1_iterf1+1),NMset1_f1x, ":r" , label = "Set1 Newton Method")
plt.plot(range(0, NMset2_iterf1+1),NMset2_f1x, "--b" , label = "Set2 Newton Method")
plt.title("f1(x) against Number of Iterations")
#Labeling the x-axis.
plt.xlabel("Number of Iterations -->")
#Labeling the y-axis.
plt.ylabel("Values of f1(x) -->")
#Setting grid properties.
plt.xticks([0,1,2,3,4])
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f1_iterationsNM", dpi=300, bbox_inches="tight")
plt.show()

plt.plot(range(0, SMset1_iterf1+1),SMset1_f1x, ":r" , label = "Set1 Secant Method")
plt.plot(range(0, SMset2_iterf1+1),SMset2_f1x, "--b" , label = "Set2 Secant Method")
#Giving a title to the graph.
plt.title("f1(x) against Number of Iterations")
#Labeling the x-axis.
plt.xlabel("Number of Iterations -->")
#Labeling the y-axis.
plt.ylabel("Values of f1(x) -->")
#Setting grid properties.
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f1_iterationsSM", dpi=300, bbox_inches="tight")
plt.show()

#f2(x) against number of iterations for both starting sets, using all 3 methods.
plt.plot(range(0, BMset1_iterf2+1), BMset1_f2x, ":b", label = "Set1 Bisection Method")
plt.plot(range(0, BMset2_iterf2+1), BMset2_f2x, "--r", label = "Set2 Bisection Method")
#Giving a title to the graph.
plt.title("f2(x) against Number of Iterations")
#Labeling the x-axis.
plt.xlabel("Number of Iterations -->")
#Labeling the y-axis.
plt.ylabel("Values of f2(x) -->")
#Setting grid properties.
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f2_iterationsBM", dpi=300, bbox_inches="tight")
plt.show()

plt.plot(range(0, NMset1_iterf2+1), NMset1_f2x, ":b" , label = "Set1 Newton Method")
plt.plot(range(0, NMset2_iterf2+1), NMset2_f2x, "--r", label = "Set2 Newton Method")
#Giving a title to the graph.
plt.title("f2(x) against Number of Iterations")
#Labeling the x-axis.
plt.xlabel("Number of Iterations -->")
#Labeling the y-axis.
plt.ylabel("Values of f2(x) -->")
#Setting grid properties.
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f2_iterationsNM", dpi=300, bbox_inches="tight")
plt.show()

plt.plot(range(0, SMset1_iterf2+1), SMset1_f2x , ":b", label = "Set1 Secant Method")
plt.plot(range(0, SMset2_iterf2+1), SMset2_f2x, "--r", label = "Set2 Secant Method")
#Giving a title to the graph.
plt.title("f2(x) against Number of Iterations")
#Labeling the x-axis.
plt.xlabel("Number of Iterations -->")
#Labeling the y-axis.
plt.ylabel("Values of f2(x) -->")
#Setting grid properties.
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f2_iterationsSM", dpi=300, bbox_inches="tight")
plt.show()

#For a given initial guess(set1), value of f1(x) against number of iterations for all three methods.
plt.plot(range(0, BMset1_iterf1+1), BMset1_f1x, ".-r", label = "Bisection Method")
plt.plot(range(0, NMset1_iterf1+1), NMset1_f1x, "s-m" , label = "Newton Method")
plt.plot(range(0, SMset1_iterf1+1), SMset1_f1x, "x-b" , label = "Secant Method")
#Giving a title to the graph.
plt.title("f1(x) against Number of Iterations for Set1")
#Labeling the x-axis.
plt.xlabel("Number of Iterations -->")
#Labeling the y-axis.
plt.ylabel("Values of f1(x) -->")
#Setting grid properties.
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f1_iterationsSet1", dpi=300, bbox_inches="tight")
plt.show()

#For a given initial guess(set1), value of f2(x) against number of iterations for all three methods.
plt.plot(range(0, BMset1_iterf2+1),BMset1_f2x, ".-r", label = "Bisection Method")
plt.plot(range(0, NMset1_iterf2+1),NMset1_f2x, "s-m" , label = "Newton Method")
plt.plot(range(0, SMset1_iterf2+1),SMset1_f2x, "x-b" , label = "Secant Method")
#Giving a title to the graph.
plt.title("f2(x) against Number of Iterations for Set1")
#Labeling the x-axis.
plt.xlabel("Number of Iterations -->")
#Labeling the y-axis.
plt.ylabel("Values of f2(x) -->")
#Setting grid properties.
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f2_iterationsSet1", dpi=300, bbox_inches="tight")
plt.show()


#For a given initial guess(set1), value of f1(x) against wall-clock time for all three methods.
plt.plot(BMset1_timef1,BMset1_f1x, ".-r", label = "Bisection Method")
plt.plot(NMset1_timef1,NMset1_f1x, "s-m" , label = "Newton Method")
plt.plot(SMset1_timef1,SMset1_f1x, "x-b" , label = "Secant Method")
#Giving a title to the graph.
plt.title("f1(x) against Wall-clock Time")
#Labeling the x-axis.
plt.xlabel("Wall-clock Time  -->")
#Labeling the y-axis.
plt.ylabel("Values of f1(x) -->")
#Setting grid properties.
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f1_Time", dpi=300, bbox_inches="tight")
plt.show()


#For a given initial guess(set1), value of f2(x) against wall-clock time for all three methods.
plt.plot(BMset1_timef2, BMset1_f2x, ".-r", label = "Bisection Method")
plt.plot(NMset1_timef2, NMset1_f2x, "s-m" , label = "Newton Method")
plt.plot(SMset1_timef2, SMset1_f2x, "x-b" , label = "Secant Method")
#Giving a title to the graph.
plt.title("f2(x) against Wall-clock Time")
#Labeling the x-axis.
plt.xlabel("Wall-clock Time  -->")
#Labeling the y-axis.
plt.ylabel("Values of f2(x) -->")
#Setting grid properties.
plt.grid(linestyle='-')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("f2_Time", dpi=300, bbox_inches="tight")
plt.show()

#Newtons method for f3(x) with the starting guess as x = 0.
NM_f3, NM_iter3, NM_f3y, timef3 = Newton_method(f3, df3, 0, 10**(-6))
print(NM_f3, NM_iter3)

