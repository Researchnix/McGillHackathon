import sys
import time

from computations import *
from constants import *
from fileWriter import *

from numpy import *
from pylab import *
from matplotlib import animation

V_tx=[]
#we first generate the V_tx matrix
for i in range(N):
    filler=[]
    for j in range(len(x_ax)):
        filler.append(V(x_ax[j],time[i]))
    filler=array(filler)
    V_tx.append(filler)
V_tx=array(V_tx)

#we construct the initial conditions


#now we begin the split step process.
F=[]
a1=f_ini
for i in range(N):
    a2=nonlinear(a1,V_tx,i)
    a3=linear(a1)
    a1=a3
    F.append(a1)
