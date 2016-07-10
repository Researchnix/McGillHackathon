import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation

filename = 'central1.txt'



hbar = 1.
m = 1.
speed = 20

dx = 0.1
dy = 0.1
dt = 0.1

N=500
time = arange(0,N*dt,dt)

L_x = 10.
L_y = 10.

x = arange( -L_x, L_x, dx)
y = arange( -L_y, L_y, dy)

u, v = meshgrid( x,y)
'''
u[i] is the x axis
v[i] is the y axis

so the pair (x[i],y[j]) is the pair  u[j,i],v[j,i]
'''
freq_x_ns = fftfreq(len(x),dx)
freq_y_ns=fftfreq(len(y),dy)
##
u_f,v_f = meshgrid(freq_x_ns, freq_y_ns)

'''
Definitin of different states
'''
def easyGauss():
    return exp( -u**2 - v**2 );

def harmonic():
    return exp( (- u **2 - v ** 2) / ( 2* hbar))

def gauss(u0, v0, ku, kv):
    return exp( (- (u - u0) **2 + 1j * u * ku - (v - v0) ** 2 ) / ( 2* hbar))

def laguerre():
    return exp(-sqrt(u**2+v**2))
    '''
def gauss(u0, v0, ku, kv):
    a = 1
    """
    a gaussian wave packet of width a, centered at x0, with momentum k0
    """ 
    return  exp(-0.5 * ((u - u0)  * 1. / a) ** 2  +
        1j * u * ku) * exp(-0.5 * ((v - v0)  * 1. / a) ** 2  + 1j * v * kv)
    '''

