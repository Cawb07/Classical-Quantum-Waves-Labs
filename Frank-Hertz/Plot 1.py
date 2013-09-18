import scipy
import numpy as np
import matplotlib.pyplot as plt

voltage, current = np.loadtxt('./lisanathan.txt', skiprows = 2, unpack=True)

plt.errorbar(voltage, current, yerr=0, fmt='bo', label="No saturation from U_1")
plt.xlabel("Voltage (10 V)")
plt.ylabel("Current (10 A)")
plt.suptitle("Voltage (V) Current (A) all uncertain by .005 V or A")
plt.legend(loc=0)

plt.show()