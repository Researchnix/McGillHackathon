import sys
import time
from numpy import *
from pylab import *
from matplotlib import animation
from constants import *


'''
    Definitin of different potentials
'''
# The harmonic potential centred at position x,y
def harmonicPot(x,y):
    return 1./2 * (x**2+y**2)

# The quartic potential centred at position x,y
def quarticPot(x,y):
    return 1./24 * (x**4+y**4 + 2* x **2 * y ** 2)

# A 1/r potential centred at position x,y with a cutoff in the centre
def centralPot(x,y):
    if abs(x)<=0.2 and abs(y)<=0.2:
        return -1./sqrt(0.2**2*2)
    else:
        return -1./sqrt(x**2+y**2)


'''
    Definitin of different wave functions
'''

# The most simple Gauss function at the origin
def easyGauss():
    return exp( -u**2 - v**2 );

# The lowest eigenstate of the harmonic potential to check if it is indeed
# in an equilibrium in the harmonic potential (it is!!) 
def harmonic():
    return exp( (- u **2 - v ** 2) / ( 2* hbar))

# The Gauss function centred at u0, v0, both float values, with momentum ku, kv,
# in the respective u,v directions
def gauss(u0, v0, ku, kv):
    return exp( (- (u - u0) **2 + 1j * u * ku - (v - v0) ** 2 ) / ( 2* hbar))

# The lowest eigenstate of the 1/r central potential centred at the position
# u0,v0
def laguerre(u0, v0):
    return exp(-sqrt((u-u0)**2+(v-v0)**2))



'''
    Methods to perform the time evolution
'''

# The nonlinear step of the Schroedinger equation, the nonlinear part is the
# potetial 
def nlStep(f_ini,V_xy,k):
    return f_ini * exp ( -1.j * V_xy*dt/hbar)

# The linear step of the Schroedinger equation, the linear part is the
# laplacian operator in the kinetic term. It is more convenient to fourier
# transform, then do the step and fourier transform back.
def fStep(f_ini):
    a1=fft2(f_ini)*exp((-1.j*(2.*pi)**2*hbar*(u_f**2+v_f**2)*dt)/(2*m))
    return ifft2(a1)
    
