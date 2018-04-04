import pickle
import scipy.io.wavfile


with open('encoded.bin','rb') as file:
    data = pickle.load(file)

#No need to dequantize
scipy.io.wavfile.write('imperial16.wav', 44100, data)
