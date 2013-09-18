import scipy
import numpy as np
import matplotlib.pyplot as plt

b = .009

V = [.163-b, .917-b, .159-b, .935-b, .106-b, .695-b, .037-b]
N = [-1.5, -1.0, -.5, 0, .5, 1.0, 1.5]

plt.errorbar(N, V, yerr=0, fmt='bo')

plt.xlabel("N (Fringe # / Position)")
plt.ylabel("Voltage (V)")
plt.suptitle("Voltages at Maxima and Minima for Double Slit Interference")
plt.legend(loc=0)

plt.show()