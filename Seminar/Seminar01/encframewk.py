# Take an audio signal and read it
import scipy.io.wavfile
import pickle
import math
import numpy as np
import sounddevice as sd

rate, data = scipy.io.wavfile.read('Imperialmono.wav')

#No need to quantize
file = open(b"encoded.bin","wb")
pickle.dump(data,file,1)
