import scipy
import numpy as np
import matplotlib.pyplot as plt

# R1 = [1.845, 1.994, 1.915, 1.783] all times 10^-5
# M1 = [2.666, 3.365, 2.981, 2.405] all times 10^-9
N = [1, 2, 3, 4]
Q = [1.787, 1.781, 1.893, 1.697] # all values times 10^-10

plt.errorbar(N, Q,  yerr=0, fmt='bo')

plt.xlabel("Q x 10^-10 (Coulombs)")
plt.ylabel("N (Rising-Falling Iteration #)")
plt.suptitle("Droplet 1")
plt.legend(loc=0)

plt.show()