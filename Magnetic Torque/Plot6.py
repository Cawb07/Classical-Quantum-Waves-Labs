import scipy 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
import platform 
import socket

b = 1.36

G = np.array([.0000003425, .000000685, .000001028, .00000137, .000001713, .000002055, .000002398, .00000274])
D = np.array([.003, .0035, .005, .008, .0095, .0115, .013, .015])

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

print LineFit(G, D)
print LineFit2(G, D)
#x = np.arange(0, 6, .1)
plt.errorbar(G, D, yerr=.0005, fmt='bo')
plt.plot(G, LineFit(G, D)*G + LineFit2(G, D))
plt.ylabel("Displacement of magnet (m)")
plt.xlabel("Gradient of magnetic field (Tesla / m)")
#plt.xlim(0, 6)            # manually set x-axis limits
#plt.ylim(0, .07)
plt.legend(loc=0)

plt.show()