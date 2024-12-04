#Fourier Transform(Noise)

#Importing required packages.
from scipy.fft import fft, ifft, fftfreq, fftshift
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics

#Selecting the font size and type to be used in the figure.
font={ 'family' : 'Times New Roman',
       'weight' : 'normal',
       'size' : '14'}

#Setting the selected font properties. 
matplotlib.rc('font', **font)

#Reading the file and storing the content in a table format.
signal = (pd.read_csv('noise.txt',sep = " ", engine = "python"))
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
yaxis_abs = np.abs(yaxis)
    
#Making the plot.
plt.plot(freq, yaxis_abs)
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
plt.savefig("Noise_fft", dpi=300, bbox_inches="tight")
plt.show()

#To find the maximum amplitudes and corresponding frequencies.
index = []
yaxis2 = yaxis_abs
#Finds the 6 highest values.
#6 because indicated by the graph.
for j in range(6):
    i = np.argmax(yaxis2)
    index.append(i)
    print(str(freq[i])+ "    " + str(yaxis2[i]))
    yaxis2[index] = 0

#Deleting the highest(true) frequencies from the signal.
new_y = np.delete(yaxis, index)
new_f = np.delete(freq, index)
#Performing inverse fast fourier transform on the signal.
new_sig = ifft(new_y)
new_time = np.delete(time, index)

#Making the plot.
plt.plot(time, signal_val, "o-b",  label = "True signal with noise")
plt.plot(new_time, new_sig, ".-r", label = "Broadband noise")
#Titling the plot.
plt.title("Inverse Fourier Transform: Noise")
#Labeling the x-axis.
plt.xlabel("Time -->")
#Setting the x values to be displayed.
plt.xlim(0.04, 0.06)
plt.xticks([0.04, 0.045, 0.05, 0.055, 0.06])
#Labeling the y-axis.
plt.ylabel("Signal -->")
#Setting grid properties.
plt.legend()
plt.grid(linestyle=':')
plt.tight_layout()
#Figure saved.
plt.savefig("Noise_time", dpi=300, bbox_inches="tight")
plt.show()

#5 point median.
time_m = [time[0], time[1]]
signal_m = [signal_val[0], signal_val[1]]
#Loop to obtain each median.
for i in range(1,997):
    med_s = statistics.median([signal_val[i-2],signal_val[i-1],signal_val[i],signal_val[i+1],signal_val[i+2]])
    signal_m.append(med_s)
    time_m.append(time[i])

#Performing fast fourier transform on the signal.
signal_mfft = fft(signal_m)
#Obtaining corresponding frequencies.
n = 998
delta_t = 0.0001001001
freq_m = fftfreq(n, delta_t)
#Shift the zero frequency component to the centre of the spectrum.
freq_m = fftshift(freq_m)
yaxis_m = fftshift(signal_mfft)
yaxis_m = np.abs(yaxis_m)

#Making the plot.
plt.plot(freq_m, yaxis_m)
#Titling the plot.
plt.title("Fourier Transform: 5 point median average")
#Labeling the x-axis.
plt.xlabel("Frequency -->")
#Labeling the y-axis.
plt.ylabel("Amplitude -->")
#Setting grid properties.
plt.grid(linestyle=':')
plt.tight_layout()
#Figure saved.
plt.savefig("Med_fft", dpi=300, bbox_inches="tight")
plt.show()

#To find the maximum amplitudes and corresponding frequencies.
index = []
yaxis2 = yaxis_m
#Finds the 6 highest values.
#6 because indicated by the graph.
for j in range(6):
    i = np.argmax(yaxis2)
    index.append(i)
    print(str(freq[i])+ "    " + str(yaxis2[i]))
    yaxis2[index] = 0
