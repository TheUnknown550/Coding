#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#Variables
sr = 44100
freq = 500
len = 10.0

t = np.arange(0, len, 1.0/sr)
signal = np.sin(np.pi * 2 * freq * t)




signal*=32767
signal = np.int16(signal)

#Show/Create Graph
plt.plot(t, signal)
plt.show()
wavfile.write("Python/OutPutFiles/FreqTest.wav",sr,signal)
