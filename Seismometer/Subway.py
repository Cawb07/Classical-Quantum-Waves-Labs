import numpy as np
from scipy.fftpack import fft, fftshift, ifft
import matplotlib.pyplot as plt

x, t = np.loadtxt('Subway.txt', skiprows = 2, unpack=True)

T = fft(t)


plt.plot(T.real)
plt.suptitle("Subway Readings (FFT)")
plt.legend(loc=0)

plt.show()