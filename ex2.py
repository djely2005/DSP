import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import remez, freqz 

fe = 4000
f = [0, 1600, 2000, fe / 2]
m = [1, 0]
w = [1, 12]

b = remez(53, f, m, weight=w, fs=fe) 
w, h = freqz(b, 1, 512, fs=fe)
plt.figure(figsize=(10, 6)) 
plt.subplot(2, 1, 1) 

plt.plot(w, 20 * np.log10(abs(h)), label="Magnitude Response (dB)")
plt.xlabel('Frequency (Hz)') 
plt.ylabel('Magnitude (dB)')
plt.title('Frequency Response of the Designed Filter')
plt.subplot(2, 1, 2) 
plt.plot(w, abs(h), label="Magnitude Response (dB)")
plt.xlabel('Frequency (Hz)') 
plt.ylabel('Magnitude') 
plt.grid() 
plt.show()