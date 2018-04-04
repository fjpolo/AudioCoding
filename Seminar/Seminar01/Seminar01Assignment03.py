#
# Seminar 1
#

#
# Assignment 1
#

# Take an audio signal and read it
import scipy.io.wavfile
import math
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

#print(chunk)
plt.figure(2)
plt.plot(data_block1)
plt.plot(data_block2)
plt.plot(data_block3)
plt.plot(data_block4)
plt.show()
#
# Assignment 4
#

# 
    
