
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
    if abs(x) < 2.:
        return 0.1
    else:
        return 0

def pot3(x):
    return 0.2*abs(x)

def pot4(x):
    if abs(x) < 2.:
        return -0.2
    else:
        return 0

def pot5(x): #we thank the mentor for this idea
    if abs(x)>4*pi:
        return 0
    if abs(x)<= 4*pi:
        return 3*sin(x/4.)
def pot6(x):
    return x**2-0.0001j


'''
now we define the nonlinear step, it will take in argument f_ini an array
of real numbers
representing the input, it will take 2D array V_tx the represents the potential.
it should should also take input integer k that tells you at what timestep you are doing this step.
'''

def nonlinear_t(f_ini,V,k):
    return f_ini*exp(-1.j*V[k]*dt/hbar)
def nonlinear_nt(f_ini,V,k):
    return f_ini*exp(-1.j*V*dt/hbar)

'''
linear fourier step
'''
def linear(f_ini):
    F1=fft(f_ini)*exp(-1.j*hbar*4.*pi**2*freq_ns**2*dt/(2*m))
    return ifft(F1)




 

