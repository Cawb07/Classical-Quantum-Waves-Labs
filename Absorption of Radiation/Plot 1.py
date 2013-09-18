import scipy
import numpy as np
import matplotlib.pyplot as plt

HV = [320, 340, 360, 380, 400, 420, 440]
N = [788, 902, 900, 906, 874, 884, 875]

plt.errorbar(HV, N,  yerr=0, fmt='bo')

plt.xlabel("Voltage (1 V)")
plt.ylabel("N (# of Counts)")
plt.suptitle("Investigating the Tube Characteristics")
plt.legend(loc=0)

plt.show()