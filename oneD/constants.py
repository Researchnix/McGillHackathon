#this contains the fundamental set up



import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation


dx=0.005
dt=0.01
hbar=.1
m=1.
#N denotes the number of time steps forward
N=5000
speed = 5
L = 20. # L, in setting up the x axis, the x axis runs from [-Lx,Lx]
plot_height = 2
x = arange(-L,L,dx)
freq_ns=fftfreq(len(x),dx)#the frequency axis unshifted
freq_sh=fftshift(freq_ns)#frequency axis shifted
time=arange(0,N*dt,dt)




#we construct the initial conditions
def easyGauss():
    return exp(-x**2)
def gauss_x(x, a, x0, k0):
        """
        a gaussian wave packet of width a, centered at x0, with momentum k0
        """ 
        return ((a * sqrt(pi)) ** (-0.5) * exp(-0.5 * ((x - x0) * 1. / a) ** 2 * + 1j * x * k0))
