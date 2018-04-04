# Take an audio signal and read it
import scipy.io.wavfile
import pickle
import math
import numpy as np
import sounddevice as sd


rate, data = scipy.io.wavfile.read('Imperialmono.wav')

#Normalization
max = np.max(data)
datan = data/float(max)

# Uniform Quantizer
stepsize=(1.0-(-1.0))/(pow(2,8))      #Stepsize
q = 256
dataq = np.round(data/q)
#datadec = dataq*q
#sd.play(datadec, rate, blocking=True)

file = open(b"encoded8bit.bin","wb")
pickle.dump(dataq,file,1)
