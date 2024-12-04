#Importing packages to use required functions.
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Selecting the font size and type to be used in the figure.
font={ 'family' : 'Times New Roman',
       'weight' : 'normal',
       'size' : '16'}

#Setting the selected font properties.          
matplotlib.rc('font', **font)

"""p=[88.29,105.95,143.23,109.87,186.39,128.51,169.71,133.42,132.44,119.68,112.82]
B = [182.47,225.14,299.25,319.05,395.57,337.67,344.65,280.19,257.34,227.21,206.54]
y=np.zeros(11)
for i in range(11):
    y[i]=279.5527272727273

plt.plot(p,B , ".g", label = "Experimental")
plt.plot(p,y , "-b", label = "Theoretical")
plt.title("Bernoulli's Equation")
#Labeling the x-axis.
plt.xlabel("Values of P -->")
#Labeling the y-axis.
plt.ylabel("Values of P +  pv^2/2-->")
plt.grid(linestyle=':')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("P1", dpi=300, bbox_inches="tight")
plt.show()

p2=[175.6,206.99,236.42,217.78,368.87,255.06,333.54,272.72,268.79,235.44,218.76]
B2=[363.18,444.45,547.05,634.38,785.47,671.66,682.24,565.14,517.48,449.85,405.27]
#Plotting and labeling the graph.
y=np.zeros(11)
for i in range(11):
    y[i]=551.47

plt.plot(p2,B2 , ".g", label = "Experimental")
plt.plot(p2,y , "-b", label = "Theoretical")
plt.title("Bernoulli's Equation")
#Labeling the x-axis.
plt.xlabel("Values of P -->")
#Labeling the y-axis.
plt.ylabel("Values of P +  pv^2/2-->")
plt.grid(linestyle=':')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("P2", dpi=300, bbox_inches="tight")
plt.show()

p2=[280.57,335.5,363.95,355.12,594.49,413,534.65,438.51,428.7,377.69,352.18]
B2=[582.43,717.7,863.55,1025.37,1264.74,1083.25,1095.5,909.15,828.85,722.6,652.42]
#Plotting and labeling the graph.
y=np.zeros(11)
for i in range(11):
    y[i]=885.96

plt.plot(p2,B2 , ".g", label = "Experimental")
plt.plot(p2,y , "-b", label = "Theoretical")
plt.title("Bernoulli's Equation")
#Labeling the x-axis.
plt.xlabel("Values of P -->")
#Labeling the y-axis.
plt.ylabel("Values of P +  pv^2/2-->")
plt.grid(linestyle=':')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("P3", dpi=300, bbox_inches="tight")
plt.show()"""

h = [0.131,0.120,0.106,0.094,0.086,0.078,0.072,0.065,0.054,0.045]
Ex = [0.008,0.007,0.014,0.013,0.012,0.008,0.006,0.007,0.003,0.004]
Th = [0.010,0.012,0.015,0.017,0.014,0.013,0.012,0.012,0.009,0.008]
#Plotting and labeling the graph.
plt.plot(h,Ex , "og", label = "Experimental")
plt.plot(h,Th , "om", label = "Theoretical")
plt.title("Hydrostatic Pressure")
#Labeling the x-axis.
plt.xlabel("Values of height h -->")
#Labeling the y-axis.
plt.ylabel("Values of delta yp -->")
plt.grid(linestyle=':')
plt.legend()
plt.tight_layout()
#Figure saved.
plt.savefig("Deltayp", dpi=300, bbox_inches="tight")
plt.show()
