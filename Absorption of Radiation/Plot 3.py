import scipy
import numpy as np
import matplotlib.pyplot as plt
plt.clf()

fig=plt.figure(1, figsize=(50,50))
fig.subplots_adjust(wspace=1.0, hspace=0.4)

B = 7.6
thickness= [4.5, 6.5, 14.1, 28.1, 59.1, 102, 129, 161, 206, 258, 419]
intensity = [(1000/(71.0*.01))-B, (1000/(71.0*.01))-B, (1000/(74.0*.01))-B, (1000/(78.0*.01))-B, (1000/(93.0*.01))-B, (1000/(97.0*.01))-B, (1000/(108.0*.01))-B, (1000/(125.0*.01))-B, (1000/(162.0*.01))-B, (1000/(207.0*.01))-B, (1000/(533.0*.01))-B]

ax1=fig.add_subplot(1,1,1)
ax1.plot(thickness, intensity)
ax1.set_yscale('log')
ax1.set_xlabel('Absorber thickness (mg/cm^2)')
ax1.set_ylabel('Log scale beam intensity (counts/minute)')
ax1.set_title('Absorption of Beta Particles')

plt.show()