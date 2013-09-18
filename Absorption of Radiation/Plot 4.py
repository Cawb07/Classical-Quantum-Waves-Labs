import scipy
import numpy as np
import matplotlib.pyplot as plt
plt.clf()

fig=plt.figure(1, figsize=(50,50))
fig.subplots_adjust(wspace=1.0, hspace=0.4)

B = 7.6
thickness= [4.5, 14.1, 59.1, 129, 206, 328, 516, 645, 1230, 3632]
intensity = [(500/(216*.01))-B, (500/(225*.01))-B, (500/(191*.01))-B, (500/(191*.01))-B, (500/(182*.01))-B, (500/(183*.01))-B, (500/(207*.01))-B, (500/(208*.01))-B, (500/(209*.01))-B, (500/(264*.01))-B]

ax1=fig.add_subplot(1,1,1)
ax1.plot(thickness, intensity)
ax1.set_yscale('log')
ax1.set_xlabel('Absorber thickness (mg/cm^2)')
ax1.set_ylabel('Log scale beam intensity (counts/minute)')
ax1.set_title('Absorption of Gamma Rays')

plt.show()