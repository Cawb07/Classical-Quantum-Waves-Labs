import scipy 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
import platform 
import socket

x = np.array([1.01, 1.57, 1.90, 2.28, 2.62, 3.00, 3.38, 3.76, 4.10, 4.53, 4.82, 5.20, 5.58, 5.88, 6.26, 6.68, 6.98, 7.32])
N = np.array([15.1, 20.0, 25.0, 30.0, 35.0, 40.0, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

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
plt.errorbar(x, N, yerr=.05, fmt='bo')
plt.plot(x, LineFit(x, N)*x + LineFit2(x, N))
plt.ylabel("Resonant Frequencies (MHz)")
plt.xlabel("Magnetic Field (mT)")
#plt.xlim(0, 6)            # manually set x-axis limits
#plt.ylim(0, .07)
plt.legend(loc=0)

plt.show()