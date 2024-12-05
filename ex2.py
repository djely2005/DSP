import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import remez, freqz 

fe = 8000
f = [0, 1600, 2000, fe / 2]
m = [1, 0]
w = [1, 12]

b = remez(53, f, m, weight=w, fs=fe) 
w, h = freqz(b, 1, 512, fs=fe)

impulse_response = np.fft.ifft(h)
phase_response = np.angle(h)
plt.plot(np.real(impulse_response), label='Real part')
plt.title("Impulse Response")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid() 
plt.legend()
plt.show()

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

# Subplot for the phase response
plt.plot(w * 2*np.pi, phase_response, label="Phase Response (dB)")
plt.title("Phase Response")
plt.xlabel("Phase")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
