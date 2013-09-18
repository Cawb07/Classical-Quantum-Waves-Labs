import scipy 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
import platform 
import socket

b = 1.36

B = np.array([1/1.36, 1/2.04, 1/2.72, 1/3.4, 1/4.08, 1/4.76, 1/5.44])
T = np.array([2.89, 1.96, 1.44, 1.1, 0.90, 0.81, 0.72])

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

print LineFit(B, T)
print LineFit2(B, T)
#x = np.arange(0, 6, .1)
plt.errorbar(B, T, yerr=.25, fmt='bo')
plt.plot(B, LineFit(B, T)*B + LineFit2(B, T))
plt.ylabel("Period Squared (s^2)")
plt.xlabel("Inverse magnitude of magnetic field at cue ball 'dipole' (Tesla)")
#plt.xlim(0, 6)            # manually set x-axis limits
#plt.ylim(0, .07)
plt.legend(loc=0)

plt.show()