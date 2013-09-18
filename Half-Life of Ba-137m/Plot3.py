import scipy
import numpy as np
import matplotlib.pyplot as plt

def LineFit(x, y):
	''' Returns slope and y-intercept of linear fit to (x,y) data set'''
	xavg = x.mean()
	slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
	yint = y.mean()-slope*xavg
	return slope

def LineFit2(x, y):
	''' Returns slope and y-intercept of linear fit to (x,y) data set'''
	xavg = x.mean()
	slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
	yint = y.mean()-slope*xavg
	return yint

n = np.array([738, 666, 594, 517, 432, 398, 312, 291, 237, 236, 179, 174, 156])
t = np.array([0., .5, 1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6.])
t2 = np.array([2.9, 2.82])

plt.errorbar(t, n, yerr=19, fmt='bo')
plt.plot(t, LineFit(t, n)*t+LineFit2(t, n))
plt.yscale('log')
plt.ylabel("Counts")
plt.xlabel("Time Lapsed Between Counts (min)")
plt.suptitle("Measuring Half-Life (Semi-Log Scale)")
plt.legend(loc=0)

plt.show()