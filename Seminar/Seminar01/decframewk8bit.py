import pickle
import scipy.io.wavfile


with open('encoded8bit.bin','rb') as file:
    dataq = pickle.load(file)

#dequantize
stepsize = (1.0-(-1.0))/(pow(2,8))
q = 256
data = (dataq*q)
data.astype(int)

scipy.io.wavfile.write('imperial8.wav', 44100, data)
