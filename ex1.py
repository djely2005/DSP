import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io import wavfile 
from scipy.signal import firwin, lfilter, freqz

# Load the audio signal (replace 'audio_with_noise.wav' with your file path)
sample_rate, noisy_signal = wavfile.read('./sound/myaudio.wav')


# Filter specifications
cutoff_freq = 2000
num_taps = 101 

# design of a lowpass filter using hamming window
lowpass_filter = firwin(num_taps, cutoff_freq, fs=sample_rate, window="hamming", pass_zero=False)

filtered_signal = lfilter(lowpass_filter, 0.001, noisy_signal)
print(filtered_signal)
w, h = freqz(lowpass_filter, worN=8000) 
frequencies = w * sample_rate / (2 * np.pi)
plt.figure(figsize=(10, 4)) 
plt.plot(frequencies, 20 * np.log10(abs(h)), 'b')
plt.title("Frequency Response of the Low-Pass FIR Filter") 
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)") 
plt.grid() 
plt.show()
plt.figure(figsize=(10, 4)) 
plt.plot(noisy_signal, color='grey', alpha=0.5, label="Original Signal (Noisy)") 
plt.plot(filtered_signal, color='blue', label="Filtered Signal")
plt.title("Time-Domain Signal (Original vs Filtered)") 
plt.xlabel("Samples")
plt.ylabel("Amplitude") 
plt.legend() 
plt.grid() 
plt.show()
wavfile.write('./sound/filtered_audio.wav', sample_rate, filtered_signal.astype(np.int16))



original_spectrum = np.fft.fft(noisy_signal) 
filtered_spectrum = np.fft.fft(filtered_signal)
freqs = np.fft.fftfreq(len(noisy_signal), 1 / sample_rate)
#Ploting The Spectrum
plt.figure(figsize=(10, 4)) 
#Original Spectrum
plt.plot(freqs[:len(freqs) // 2], 20 * np.log10(np.abs(original_spectrum[:len(freqs) //2])), 'grey', alpha=0.5, label="Original")
#Filtered Spectrum
plt.plot(freqs[:len(freqs) // 2], 20 * np.log10(np.abs(filtered_spectrum[:len(freqs) //2])), 'blue', label="Filtered")
plt.title("Frequency Spectrum (Original vs Filtered)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)") 
plt.legend() 
plt.grid() 
plt.show()