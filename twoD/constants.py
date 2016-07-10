import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation

'''
    Set all relevant constants here 
'''
# The filename to which the data will be saved
filename = 'lattice1'
# The speed of the animation
speed = 150
# total number of time steps to be performed, i.e total time of evolution 
N=100
# time step size
dt = 0.1
time = arange(0,N*dt,dt)

################## PHYSICAL CONSTANTS ################## 
hbar = 1.
# particle mass
m = 1.
# mesh size
dx = 0.1
dy = 0.1
# total size of the grid
L_x = 10.
L_y = 10.
# The grid x,y and the resulting meshgrid u,v
x = arange( -L_x, L_x, dx)
y = arange( -L_y, L_y, dy)
u, v = meshgrid( x,y)

# The grid in fourier space
freq_x_ns = fftfreq(len(x),dx)
freq_y_ns = fftfreq(len(y),dy)
# The meshgrid in fourier space
u_f,v_f = meshgrid(freq_x_ns, freq_y_ns)

