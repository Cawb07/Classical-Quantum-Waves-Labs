import scipy
import numpy as np
import matplotlib.pyplot as plt

# R2 = [2.612, 2.184, 2.184, 2.184] all times 10^-5
# M2 = [7.563, 4.421, 4.421, 4.421] all times 10^-9
N = [1, 2, 3, 4]
Q = [2.891, 3.240, 3.240, 3.240] # all values times 10^-10

plt.errorbar(N, Q,  yerr=0, fmt='bo')

plt.xlabel("Q x 10^-10 (Coulombs)")
plt.ylabel("N (Rising-Falling Iteration #)")
plt.suptitle("Droplet 2")
plt.legend(loc=0)

plt.show()