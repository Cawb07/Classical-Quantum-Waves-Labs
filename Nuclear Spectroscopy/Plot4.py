import scipy 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
import platform 
import socket

N = np.array([399, 362, 318])
x = np.array([0, .003, .007])

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

print LineFit(x, N)
print LineFit2(x, N)
#x = np.arange(0, 6, .1)
plt.errorbar(x, N, yerr=19, fmt='bo')
plt.plot(x, LineFit(x, N)*x + LineFit2(x, N))
plt.ylabel("Counts in Integration Range")
plt.xlabel("Absorber Thickness (m)")
#plt.xlim(0, 6)            # manually set x-axis limits
#plt.ylim(0, .07)
plt.legend(loc=0)

plt.show()