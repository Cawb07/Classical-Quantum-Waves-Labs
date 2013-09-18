import scipy 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
import platform 
import socket

b = 1.36

B = np.array([3.4, 3.8, 4.2, 4.6, 5.0, 5.4])
r = np.array([.041, .044, .047, .049, .050, .051])

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

print LineFit(B, r)
print LineFit2(B, r)
x = np.arange(0, 6, .1)
plt.errorbar(B, r, yerr=.0005, fmt='bo')
plt.plot(x, LineFit(B, r)*x + LineFit2(B, r))
plt.ylabel("Position of handle weight (m)")
plt.xlabel("Magnitude of magnetic field at cue ball 'dipole' (Tesla)")
plt.xlim(0, 6)            # manually set x-axis limits
plt.ylim(0, .07)
plt.legend(loc=0)

plt.show()