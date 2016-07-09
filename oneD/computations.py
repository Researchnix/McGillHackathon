
import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation
from constants import *

'''
We define here the potential function, input takes (x,t) x is position t is time
the matrix will be computed in the main program. the potential is complex valued
'''

def pot1(x,t):
    if t<0.5:
        return 0.1 * x**2
    if t>=0.5:
        return 0.1 * x ** 2 + x

def pot2(x):
    if abs(x) < L * 0.1:
        return 0
    else:
        return 10

def pot3(x):
    return abs(x)
        


'''
now we define the nonlinear step, it will take in argument f_ini an array
of real numbers
representing the input, it will take 2D array V_tx the represents the potential.
it should should also take input integer k that tells you at what timestep you are doing this step.
'''

def nonlinear(f_ini,V,k):
    return f_ini*exp(-1.j*V*dt/hbar)


'''
linear fourier step
'''
def linear(f_ini):
    F1=fft(f_ini)*exp(-1.j*hbar*4.*pi**2*freq_ns**2*dt/(2*m))
    return ifft(F1)

 
