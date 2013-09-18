import scipy 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
import platform 
import socket

b = 1.36

B = np.array([1.36, 2.04, 2.72, 3.4, 4.08, 4.76, 5.44])
O = np.array([18.3, 20.0, 20.0, 20.4, 21.4, 22.0, 22.4])

def LineFit(x, y):
	''' Returns slope of linear fit to (x,y) data set'''
	xavg = x.mean()
	slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
	yint = y.mean()-slope*xavg
	return slope

def LineFit2(x, y):
	''' Returns y-intercept of linear fit to (x,y) data set'''
	xavg = x.mean()
	slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
	yint = y.mean()-slope*xavg
	return yint

print LineFit(B, O)
print LineFit2(B, O)
#x = np.arange(0, 6, .1)
plt.errorbar(B, O, yerr=1, fmt='bo')
plt.plot(B, LineFit(B, O)*B + LineFit2(B, O))
plt.ylabel("Angular Frequency (radians / s)")
plt.xlabel("Magnitude of magnetic field at cue ball 'dipole' (Tesla)")
#plt.xlim(0, 6)            # manually set x-axis limits
#plt.ylim(0, .07)
plt.legend(loc=0)

plt.show()