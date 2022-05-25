#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#Variables
sr = 44100
freq = 500
len = 1.0

t = np.arange(0, len, 1.0/sr)
signal = np.sin(np.pi * 2 * freq * t)


plt.plot(t, signal)
plt.show()

signal*=32767
signal = np.int16(signal)
wavfile.write("Python/OutPutFiles/FreqTest.wav",sr,signal)
