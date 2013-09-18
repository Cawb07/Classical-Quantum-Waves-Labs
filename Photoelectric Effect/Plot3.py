import scipy
import numpy as np
import matplotlib.pyplot as plt

voltage, deflection = np.loadtxt('./plot3.txt', skiprows = 2, unpack=True)

plt.errorbar(voltage, deflection, yerr=0, fmt='bo')
plt.xlabel("Voltage (V +- .0005 V)")
plt.ylabel("Deflection (mm +- .5 mm)")
plt.suptitle("577.0 nm filter")
plt.legend(loc=0)

plt.show()