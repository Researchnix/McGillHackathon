import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation

filename = 'doublecentral1'



hbar = 1.
m = 1.
speed = 50

dx = 0.04
dy = 0.04
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

