import scipy
import numpy as np
import matplotlib.pyplot as plt

f = [6.884, 5.495, 5.199] #all times 10^14
Vs = [1.143, .644, .541]

fig = plt.figure(1, figsize=(9,8))
fig.subplots_adjust(wspace=0.3, hspace=0.3)

ax1 = fig.add_subplot(2,2,1)
ax1.errorbar(f, Vs, yerr=0, fmt='bo')
ax1.set_xlabel('Frequency (10^14 Hz)')
ax1.set_ylabel('Stopping Voltage (V +- .0005 V)')
ax1.set_title("Extrapolating Planck's constant and the work function")

ax2 = fig.add_subplot(2,2,2)
ax2.plot(f, Vs)
ax2.set_xlabel('Frequency (10^14 Hz)')
ax2.set_ylabel('Stopping Voltage (V +- .0005 V')
ax2.set_title('Line Fit')

#plt.errorbar(f, Vs, yerr=0, fmt='bo')
#plt.xlabel("Frequency (Hz)")
#plt.ylabel("Stopping Voltage (V +- .0005 V)")
#plt.suptitle("Extrapolating Planck's constant and the work function")
#plt.legend(loc=0)

plt.show()