import numpy as np 
import matplotlib.pyplot as plt 
from scipy.signal import freqz, firwin2
# Parameters
fs = 8000 
H1 = [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0] 
H2 = [0, 0, 0, 0, 0.5, 1, 1, 1, 1, 0.5, 0, 0, 0]
B1 = firwin2(25, np.linspace(0, 1, len(H1)), H1) 
B2 = firwin2(25, np.linspace(0, 1, len(H2)), H2) 
w, h1 = freqz(B1, 1, 512, fs=fs) 
_, h2 = freqz(B2, 1, 512, fs=fs)
p1 = np.unwrap(np.angle(h1)) * (180 / np.pi) 
p2 = np.unwrap(np.angle(h2)) * (180 / np.pi)
plt.figure(figsize=(10, 8)) 
plt.subplot(2, 1, 1) 
plt.plot(w, 20 * np.log10(abs(h1)), label="Filter 1") 
plt.plot(w, 20 * np.log10(abs(h2)), label="Filter 2") 
plt.grid()
plt.axis([0, fs / 2, -100, 10]) 
plt.xlabel('Frequency (Hz)') 
plt.ylabel('Magnitude Response (dB)') 
plt.legend() 
plt.subplot(2, 1, 2) 
plt.plot(w, p1, label="Filter 1")
plt.plot(w, p2, label="Filter 2") 
plt.grid() 
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)') 
plt.legend() 
plt.tight_layout() 
plt.show()