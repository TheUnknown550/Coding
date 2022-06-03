import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

FileName = 'D:/Projects/Coding/Python/3.9/Sound/Sounds/File.wav'

# read ECG data from the WAV file
sampleRate, data = scipy.io.wavfile.read(FileName)
times = np.arange(len(data))/sampleRate

# apply a 3-pole lowpass filter at 0.1x Nyquist frequency
b, a = scipy.signal.butter(10, 0.1)
filtered = scipy.signal.filtfilt(b, a, data)

# plot the original data next to the filtered data


plt.plot(times, data,  label='Original')
plt.plot(times, filtered, label='Filtered')

plt.legend()
plt.show()