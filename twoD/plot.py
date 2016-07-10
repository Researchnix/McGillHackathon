from constants import *
from computations import *
from fileWriter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

F = []          # 3 dim
def loadData(filename):
    print 'Loading the data ...'
    mat = []        # 2 dim
    with open(filename, 'r') as f:
        for line in f:
            if line != '\n':
                row = map(float, line.split())
                mat.append(row)
            else:
                F.append(mat)
                print 'norm stuff... ' + str(sum(array(mat)) / sum(array(F[0])))
                mat = []
        F.append(mat)

def plotPot(V):

    fig = plt.figure()
    im = plt.imshow(V, animated=True)
    plt.colorbar(im)
    show()



def plotColor():

    fig = plt.figure()

    z = F[0]
    im = plt.imshow(z, animated=True)
    plt.clim(0,1)
    plt.colorbar(im)


    def updatefig(i):
        im.set_array(F[i])
        return im,

    ani = animation.FuncAnimation(fig, updatefig, interval=speed, blit=True)
    show()


def plotThreeD():
    def data(i, z, line):
        z = F[i]
        ax.clear()
        ax.set_zlim((0,1))
        line = ax.plot_surface(u,v, z)
        return line,

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
     
    z = F[0]
    line = ax.plot_surface(u, v, z)
    ax.set_zlim((0,1))

    ani = animation.FuncAnimation(fig, data, fargs = (z, line), interval = speed, blit =
            False)
    show()

