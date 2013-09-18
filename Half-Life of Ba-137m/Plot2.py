import scipy
import numpy as np
import matplotlib.pyplot as plt

n = [738, 666, 594, 517, 432, 398, 312, 291, 237, 236, 179, 174, 156]
t = [0., .5, 1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6.]

plt.errorbar(t, n, yerr=19.5, fmt='bo')
#plt.yscale('log')
plt.ylabel("Counts")
plt.xlabel("Time Lapsed Between Counts (min)")
plt.suptitle("Measuring Half-Life")
plt.legend(loc=0)

plt.show()