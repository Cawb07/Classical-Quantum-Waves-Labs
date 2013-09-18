# Reads in data from data file, plots it and compares it to
# an exponentially decaying sinusoidal signal
import numpy as np
import matplotlib.pyplot as plt

# Function defining exponentially decaying sinusoidal
def thetaU(t, A, w0, Q, phi):
	wu = w0 * np.sqrt(1.0-1.0/(4.0*Q*Q))
	return A * np.exp(-0.5*w0*t/Q) * np.sin(wu*t + phi)

# User sets these parameters to best match the data
A = 0.6 # Amplitude
T = 12.6 # Period (w0 = 2 pi / T)
Q = .55 # Q = quality factor (determines damping)
phase = 0. # phase in degrees

# Convert phase in degrees to phase in radius for use in function
phi = np.pi * phase / 180.0 # phase in radians
time, theta = np.loadtxt('Q6.txt', skiprows=30, unpack=True)
fit = thetaU(time, A, 2.0*np.pi/T, Q, phi)
plt.plot(time, fit)
plt.axhline(color='gray')
plt.plot(time, theta)

plt.show()
