from pylab import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

from constants import *
from computations import *



f_ini = easyGauss()

V_txy = zeros((N,len(x), len(y)))
F=[]
a1=f_ini
for i in range(N):
    a2=nlStep(a1,V_txy,i)
    a3=fStep(a2)
    a1=a3
    F.append(abs(a1)**2)
    
    
    

"""
Plot the result
"""
def data(i, z, line):
    z = F[i]
    ax.clear()
    line = ax.plot_surface(u,v, z)
    return line,

n = 2 * pi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
z = F[0]
line = ax.plot_surface(u, v, z)

ani = animation.FuncAnimation(fig, data, fargs = (z, line), interval = 30, blit =
        False)
show()
