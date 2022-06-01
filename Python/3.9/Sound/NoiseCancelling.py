# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from scipy.io import wavfile
 
# shows the sound waves
def visualize(path: str):
    RecTime = []
    RecSig = []
    CheckSigHigh= []
    CheckTimeHigh= []
    CheckTimeLow= []
    CheckSigLow= []
    counter = 0
    counters = 0
    TimeHighPoint = 0
    SumTimeHighPoint = 0
    TimeHighMax = 0
    TimeHighMin = 0
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
        
        if signal [i] > 2750:
            CheckSigHigh.append(signal[i])
            CheckTimeHigh.append(round(time[i],3))
            if counter == 0:
                counter = 1
            
        
        if signal[i] < 2750 and counter == 1:
            #Way 1 use Time Avg per each graph
            for n in range (len(CheckTimeHigh)):
                SumTimeHighPoint = SumTimeHighPoint + CheckTimeHigh[n]
            TimeHighPoint = SumTimeHighPoint/int(len(CheckTimeHigh))
            SumTimeHighPoint = 0

            #Way 2 use (highest + min) /2
            '''CheckTimeHigh.sort(reverse=True)
            TimeHighMax = CheckTimeHigh[0]
            TimeHighMin = CheckTimeHigh[int(len(CheckTimeHigh))-1]
            TimeHighPoint = (TimeHighMax + TimeHighMin) / 2'''

            #Both Works Well

            #Find Highest Point of signal
            CheckSigHigh.sort(reverse=True)

            #Add the highest variables to list
            RecTime.append(TimeHighPoint)
            RecSig.append(CheckSigHigh[0])

            #Resets variables for later use
            TimeHighPoint = 0
            counter = 0
            
            #Clear list for later use
            CheckSigHigh.clear()
            CheckTimeHigh.clear()



        if signal [i] < -2600:
            CheckSigLow.append(signal[i])
            CheckTimeLow.append(round(time[i],3))
            if counter == 0:
                counter = 1

        if signal[i] > -2600 and counter == 1:
            for m in range (len(CheckTimeLow)):
                SumTimeLowPoint = SumTimeLowPoint + CheckTimeLow[m]
            TimeLowPoint = SumTimeLowPoint/int(len(CheckTimeLow))
            SumTimeLowPoint = 0

            #Find Highest Point of signal
            CheckSigLow.sort(reverse=True)

            #Add the highest variables to list
            RecTime.append(TimeLowPoint)
            RecSig.append(CheckSigLow[0])

            #Resets variables for later use
            TimeLowPoint = 0
            counter = 0
            
            #Clear list for later use
            CheckSigLow.clear()
            CheckTimeLow.clear()

        if signal[i] == 0:
            RecTime.append(round(time[i],3))
            RecSig.append(signal[i])

    '''print(RecTime)
    print(len(RecTime))
    print(RecSig)
    print(len(RecSig))'''
    # using matplotlib to plot
    # creates a new figure
    plt.figure(1)
     
    # title of the plot
    plt.title("Sound Wave")
     
    # label of x-axis
    plt.xlabel("Time")
    
    # actual plotting
    plt.plot(time, signal)
    plt.plot(RecTime, RecSig)
    # shows the plot
    # in new window
    plt.show()
    #wavfile.write("Python/OutPutFiles/SigTest.wav",RecTime,RecSig)
    # you can also save
    # the plot using
    # plt.savefig('filename')
 

if __name__ == "__main__":
   
    # gets the command line Value
    path = 'D:/Projects/Coding/Python/3.9/Sound/Sounds/a0001.wav'
 
    visualize(path)