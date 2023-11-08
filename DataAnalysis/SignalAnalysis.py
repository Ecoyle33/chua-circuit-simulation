#Need a dataframe for the 2d V1-V2 phase space, no need to analyse current for the capacitors
#Need to consider getting Data for the V-I characteristic of the Chua Diode

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fft import fft, fftfreq


#1-Input Signal (V), 2- Encrypted Signal (V), 3-Output Signal (V), 4-Chua Signal (V)
#df = dataframe for encrypted signal voltages, use file path  
df = pd.read_csv(r"C:\Users\euanc\OneDrive - University of Bath\Documents\Work\Final Year\Final Year Project\Data\Data Analysis\Data\WFM6.CSV", header=None, names=["Time (s)", "Ch 1", "Ch 2", "Ch 3", "Ch 4"])
data = df[df["Time (s)"].between(0, 10)]
#data = df[:200000]

EncryptionStrength = data["Ch 2"] - data["Ch 4"]

Noise = data["Ch 3"]-data["Ch 1"]

"""
plt.plot(data["Time (s)"], EncryptionStrength, linewidth = 1)
plt.xlim([-8.6, -8.3])
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
"""

#plt.plot(df["Time (s)"], df["Ch 4"], color="black", linewidth=1)

fig1, axs1 = plt.subplots(4, sharex=True)
axs1[0].plot(data["Time (s)"], data["Ch 1"])
axs1[1].plot(data["Time (s)"], data["Ch 2"])
axs1[2].plot(data["Time (s)"], data["Ch 3"])
axs1[3].plot(data["Time (s)"], data["Ch 4"])

axs1[0].set(ylabel = 'Ch 1')
axs1[1].set(ylabel = 'Ch 2')
axs1[2].set(ylabel = 'Ch 3')
axs1[3].set(ylabel = 'Ch 4')

axs1[3].set(xlabel = 'Time (s)')
axs1[0].set_ylim([-0.75, 1.25])
axs1[2].set_ylim([-2, 2.5])
#axs1[3].set_xlim([5, 10])

"""
plt.plot(data["Time (s)"], Noise, linewidth = 1)
plt.xlim([-8.6, -8.3])
plt.xlabel("Time (s)")
plt.ylabel("Noise (V)")
"""

fig2, axs2 = plt.subplots(3, sharex=True)
axs2[0].plot(data["Time (s)"], data["Ch 3"])
axs2[1].plot(data["Time (s)"], data["Ch 1"])
axs2[2].plot(data["Time (s)"], Noise)
#axs2[2].set_xlim([5, 10])

#----------------Fourier Analysis----------------------
ftCH1 = fft(np.array(data["Ch 1"]))
ftCH2 = fft(np.array(data["Ch 2"]))
ftCH3 = fft(np.array(data["Ch 3"]))
ftChua = fft(np.array(data["Ch 4"]))
ftNoise = fft(np.array(Noise))

N = 27233  #Number of sample points

T = 0.02 

t = np.linspace(0, T, N, endpoint=False)
dt = np.diff(t)[0]
f = fftfreq(len(t), np.diff(t)[0])

xf = 1/t
freq = xf / 1e3

fig3, axs3 = plt.subplots(5, sharex=True)
axs3[0].plot(freq[:N//2], np.abs(ftCH1[:N//2]))
axs3[1].plot(freq[:N//2], np.abs(ftCH2[:N//2]))
axs3[2].plot(freq[:N//2], np.abs(ftCH3[:N//2]))
axs3[3].plot(freq[:N//2], np.abs(ftChua[:N//2]))
axs3[4].plot(freq[:N//2], np.abs(ftNoise[:N//2]))
axs3[0].set(ylabel = 'FFT CH1 (V^-1)')
axs3[1].set(ylabel = 'FFT CH2 (V^-1)')
axs3[2].set(ylabel = 'FFT CH3 (V^-1)')
axs3[3].set(ylabel = 'FFT Chua (V^-1)')
axs3[4].set(ylabel = 'FFT Noise (V^-1)')
axs3[4].set(xlabel = 'Frequency (kHz)')
axs3[4].set_xlim([0, 20])
plt.show()
