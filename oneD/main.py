import sys
import time

from computations import *
from constants import *
from fileWriter import *

from numpy import *
from pylab import *
from matplotlib import animation

V=[]
#we first generate the V matrix V is time dependent

V = map(pot6,x)
'''
for k in range(N):
    b=[]
    for i in range(len(x)):
        b.append(pot5(x[i],time[k]) + 0.j)
    b=array(b)
    V.append(b)
    
'''    
V=array(V)
print('done potential')
#we construct the initial conditions


#now we begin the split step process.
F=[]


for i in range(N):
    a2=nonlinear_nt(a1,V,i)
    a3=linear(a2)
    a1=a3
    if i%50==0:
        if abs(abs(trapz(abs(a1)**2,x)/Norm)-1)>0.1:
            print "you should probably stop here", i
    F.append(abs(a1)**2)


def init():
    line.set_data([], [])
    step_text.set_text('')
    norm_text.set_text('')
    return line, step_text,norm_text

def animate(i):
    y =F[i]
    line.set_data(x, y)
    step_text.set_text("steps: " + str(i))
    #norm_text.set_text("percentage deviation from initial norm: " + str(abs(abs(trapz(F[i],x)/Norm)-1)))
    norm_text.set_text("percentage deviation from initial norm: " + str(abs(abs(trapz(F[i],x)/Norm))))
    return line, step_text, norm_text



fig = figure()
ax = axes(xlim=(-L, L), ylim=(-1, plot_height))
line, = plot([], [], lw=2)
step_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
norm_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=N, interval=speed, blit=True)
plot(x, V)
show()


