import scipy
import numpy as np
import matplotlib.pyplot as plt

n = [1.0001785, 1.00021125]
w = [510., 650.]

plt.errorbar(w, n, yerr=.000003377, fmt='bo')
plt.ylabel("Index of Refraction of Air")
plt.xlabel("Wavelength of Light (nm)")
plt.legend(loc=0)

plt.show()