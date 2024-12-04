#Fourier Transform

#Importing required packages.
from scipy.fft import fft, ifft, fftfreq, fftshift
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Selecting the font size and type to be used in the figure.
font={ 'family' : 'Times New Roman',
       'weight' : 'normal',
       'size' : '14'}

#Setting the selected font properties. 
matplotlib.rc('font', **font)

#Reading the file and storing the content in a table format.
signal = (pd.read_csv('signal.txt',sep = " ", engine = "python"))
#Extracting the columns in the file.
time = signal['time'].tolist()
signal_val = signal['signal_value'].tolist()
#Performing fast fourier transform on the signal.
signal_fft = fft(signal_val)
#Obtaining corresponding frequencies.
n = 1000
delta_t = 0.0001001001
freq = fftfreq(n, delta_t)
#Shift the zero frequency component to the centre of the spectrum.
freq = fftshift(freq)
yaxis = fftshift(signal_fft)
    
#Making the plot.
plt.plot(freq, np.abs(yaxis))
#Titling the plot.
plt.title("Fourier Transform")
#Labeling the x-axis.
plt.xlabel("Frequency -->")
#Labeling the y-axis.
plt.ylabel("Amplitude -->")
#Setting grid properties.
plt.grid(linestyle=':')
plt.tight_layout()
#Figure saved.
plt.savefig("Signal_fft", dpi=300, bbox_inches="tight")
plt.show()

#To find the maximum amplitudes and corresponding frequencies.
index = []
yaxis2 = np.abs(yaxis)
#Finds the 10 highest values.
#10 because indicated by the graph.
for j in range(10):
    i = np.argmax(yaxis2)
    index.append(i)
    print(str(freq[i])+ "    " + str(yaxis2[i]))
    yaxis2[index] = 0
