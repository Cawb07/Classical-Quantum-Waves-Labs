import scipy 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
import platform 
import socket

b = 1.36

F = np.array([.0098, .0196])
D = np.array([.004, .011])

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

print LineFit(F, D)
print LineFit2(F, D)
#x = np.arange(0, 6, .1)
plt.errorbar(F, D, yerr=.0005, fmt='bo')
plt.plot(F, LineFit(F, D)*F + LineFit2(F, D))
plt.ylabel("Displacement of magnet (m)")
plt.xlabel("Force on magnet (N)")
#plt.xlim(0, 6)            # manually set x-axis limits
#plt.ylim(0, .07)
plt.legend(loc=0)

plt.show()