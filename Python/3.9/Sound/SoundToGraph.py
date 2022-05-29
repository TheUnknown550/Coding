# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
 
# shows the sound waves
def visualize(path: str):
    RecTime = []
    RecSig = []
    CheckSig= []
    CheckTime= []
    TimeLen = 0
    counter = 0
    counters = 0
    # reading the audio file
    raw = wave.open(path)
     
    # reads all the frames
    # -1 indicates all or max frames
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")
    
    
    
    # gets the frame rate
    f_rate = raw.getframerate()
 
    # to Plot the x-axis in seconds
    # you need get the frame rate
    # and divide by size of your signal
    # to create a Time Vector
    # spaced linearly with the size
    # of the audio file
    time = np.linspace(
        0, # start
        len(signal) / f_rate,
        num = len(signal)
    )
    #Note!! play with signal instead of time
    for i in range(len(signal)):
        if signal[i] > 3700 and counter == 0:
            RecTime.append(round(time[i],3))
            RecSig.append(signal[i])
            counter = 1

        elif signal[i] < 3700 and counter == 1: 
            counter = 0

        if signal[i] > -2850 and counters == 0:
            RecTime.append(round(time[i],3))
            RecSig.append(signal[i])
            counters = 1

        elif signal[i] < -2850 and counters == 1: 
            counters = 0

        if signal[i] == 0:
            RecTime.append(round(time[i],3))
            RecSig.append(signal[i])

    print(RecTime)
    print(len(RecTime))
    print(RecSig)
    print(len(RecSig))
    # using matplotlib to plot
    # creates a new figure
    plt.figure(1)
     
    # title of the plot
    plt.title("Sound Wave")
     
    # label of x-axis
    plt.xlabel("Time")
    
    # actual plotting
    #plt.plot(time, signal)
    plt.plot(RecTime, RecSig)
    # shows the plot
    # in new window
    plt.show()
    wavfile.write("Python/OutPutFiles/FreqTest.wav",RecTime,RecSig)
    # you can also save
    # the plot using
    # plt.savefig('filename')
 

if __name__ == "__main__":
   
    # gets the command line Value
    path = 'D:/Projects/Coding/Python/3.9/Sound/Sounds/a0001.wav'
 
    visualize(path)