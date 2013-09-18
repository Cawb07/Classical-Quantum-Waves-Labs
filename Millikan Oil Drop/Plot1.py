import scipy
import numpy as np
import matplotlib.pyplot as plt

# R = [1.99, 2.18, 2.44, 2.08, 2.18] all times 10^-5
# M = [3.345, 4.397, 6.166, 3.819, 4.397] all timess 10^-9
N = [1, 2, 3, 4, 5]
Q = [1.377, 1.260, 1.958, 1.027, 1.034] # all values times 10^-10

plt.errorbar(N, Q,  yerr=0, fmt='bo')

plt.xlabel("Q x 10^-10 (Coulombs)")
plt.ylabel("N (Droplet #)")
plt.suptitle("Charges of 5 seperate droplets")
plt.legend(loc=0)

# II Now all readings are with one droplet
# R1 = [1.845, 1.994, 1.915, 1.783] all times 10^-5
# M1 = [2.666, 3.365, 2.981, 2.405] all times 10^-9
# R2 = [2.612, 2.184, 2.184, 2.184] all times 10^-5
# M2 = [7.563, 4.421, 4.421, 4.421] all times 10^-9



plt.show()