import scipy
import numpy as np
import matplotlib.pyplot as plt

n = [175, 51, 20, 6, 7, 5, 7]
d = [0, 5, 10, 15, 20, 25, 30]

plt.errorbar(d, n, yerr=6.2, fmt='bo')
plt.ylabel("Counts")
plt.xlabel("Distance of Source from Counter (cm)")
plt.suptitle("Measuring the Strength of the Source")
plt.legend(loc=0)

plt.show()