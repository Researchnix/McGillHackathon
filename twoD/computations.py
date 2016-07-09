import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation
from constants import *


def V(x,y,t):
    return x**2+y**2

def nlStep(f_ini,V_txy,k):
    return f_ini * exp ( -1.j * V_txy[k]*dt/hbar)

def fStep(f_ini):
    a1=fft2(f_ini)*exp(-1.j*(2.*pi)**2*hbar*(u_f**2+v_f**2)*dt)
    return ifft2(a1)
    
