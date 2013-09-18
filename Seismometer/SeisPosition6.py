import scipy
import numpy as np
import matplotlib.pyplot as plt

x, t = np.loadtxt('Q6.txt', skiprows = 2, unpack=True)

plt.errorbar(x, t, yerr=0)
plt.xlabel("Time")
plt.ylabel("Position")
plt.suptitle("Critically Damped")
plt.legend(loc=0)

plt.show()