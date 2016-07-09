#this contains the fundamental set up



import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation


dx=0.01
dt=0.01
hbar=0.1
m=1.
#N denotes the number of time steps forward
N=500
L_x=5. # L_x, in setting up the x axis, the x axis runs from [-Lx,Lx]
x_ax=arange(-L_x,L_x,dx)
freq_ns=fftfreq(len(x_ax),dx)#the frequency axis unshifted
freq_sh=fftshift(freq_ns)#frequency axis shifted
time=arange(0,N*dt,dt)

#we construct the initial conditions

f_ini=exp(-x_ax**2)
