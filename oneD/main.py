import sys
import time

from computations import *
from constants import *
from fileWriter import *

from numpy import *
from pylab import *
from matplotlib import animation

V=[]
#we first generate the V matrix
'''
for i in range(N):
    filler=[]
    for j in range(len(x_ax)):
        filler.append(V(x_ax[j],time[i]))
    filler=array(filler)
    V.append(filler)
'''
#V = map(pot2,x)
for i in range(len(x)):
    V.append(pot3(x[i]) + 0.j)
    #V.append(0 + 0.j)
V=array(V)

#we construct the initial conditions


#now we begin the split step process.
F=[]
a1 = easyGauss()
for i in range(N):
    a2=nonlinear(a1,V,i)
    a3=linear(a2)
    a1=a3
    F.append(abs(a1)**2)


def init():
    line.set_data([], [])
    step_text.set_text('')
    return line, step_text

def animate(i):
    y =F[i]
    line.set_data(x, y)
    step_text.set_text("steps: " + str(i))
    return line, step_text



fig = figure()
ax = axes(xlim=(-2*L, 2*L), ylim=(-1, plot_height))
line, = plot([], [], lw=2)
step_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=N, interval=speed, blit=True)
plot(x, V)
show()
