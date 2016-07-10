import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation
from constants import *


'''
Definitin of different potentials
'''
def harmonicPot(x,y):
    return 1./2 * (x**2+y**2)

def quarticPot(x,y):
    return 1./24 * (x**4+y**4 + 2* x **2 * y ** 2)

def centralPot(x,y):
    if abs(x)<=0.2 and abs(y)<=0.2:
        return -1./sqrt(0.2**2*2)
    else:
        return -1./sqrt(x**2+y**2)
'''
Definitin of different states
'''
def easyGauss():
    return exp( -u**2 - v**2 );

def harmonic():
    return exp( (- u **2 - v ** 2) / ( 2* hbar))

def gauss(u0, v0, ku, kv):
    return exp( (- (u - u0) **2 + 1j * u * ku - (v - v0) ** 2 ) / ( 2* hbar))

def laguerre(u0, v0):
    return exp(-sqrt((u-u0)**2+(v-v0)**2))



def nlStep(f_ini,V_xy,k):
    return f_ini * exp ( -1.j * V_xy*dt/hbar)

def fStep(f_ini):
    a1=fft2(f_ini)*exp((-1.j*(2.*pi)**2*hbar*(u_f**2+v_f**2)*dt)/(2*m))
    return ifft2(a1)
    
