#
# Seminar 1
#

#
# Assignment 1
#

# Take an audio signal and read it
import scipy.io.wavfile
import math
import scipy.fftpack

rate, data = scipy.io.wavfile.read('Imperialmono.wav')
print(rate)
print(len(data))

# Play audio signal
import sounddevice as sd
#sd.play(data, rate, blocking=True)

# Extract 4 seconds from the middle of the audio data
# 4[s]*44100[sps] = 176400
# Middle = 442541/2 = 221270
# Extract 221270 to 397670
import numpy as np
import matplotlib.pyplot as plt

data4s = data[221270:397670:1]
print(len(data4s))
#sd.play(data4s, rate, blocking=True)
max = np.max(data4s)
print(max)                                          # Max = 26203
data4s_norm = tuple(i/float(max) for i in data4s)         # Normalize
# Plot
plt.figure(1)
plt.plot(data4s_norm)
plt.show()

#
# Assignment 2
#

# Process it block wise, by taking 4 consecutive blocks of 1024 samples
# Apply the FFT to it
# Plot the magnitude of it (The 4 different FFT blocks in different colors on top of each other)

# 176400/1024 = 172*1024 + 272 = 176128 + 272
data_block1 = data4s_norm[0:1024:1]
data_block2 = data4s_norm[1025:20148:1]
data_block3 = data4s_norm[2049:3072:1]
data_block4 = data4s_norm[3073:4096:1]

fftblock1 = np.fft.fft(data_block1)
fftblock1 = fftblock1[range(512)]
fftblock1 = abs(fftblock1)
fftblock2 = np.fft.fft(data_block2)
fftblock2 = fftblock2[range(512)]
fftblock2 = abs(fftblock2)
fftblock3 = np.fft.fft(data_block3)
fftblock3 = fftblock3[range(512)]
fftblock3 = abs(fftblock3)
fftblock4 = np.fft.fft(data_block4)
fftblock4 = fftblock4[range(512)]
fftblock4 = abs(fftblock4)

# 44100 SPS
# 1024 SPB
# t = 23,22mS
t = np.ones(1024)
dif = 23.22/1024
t = t*dif
#freq = np.fft.fftfreq(t.shape[-1])

#print(chunk)
plt.figure(2)
plt.plot(fftblock1)
plt.plot(fftblock2)
plt.plot(fftblock3)
plt.plot(fftblock4)
plt.show()


    
