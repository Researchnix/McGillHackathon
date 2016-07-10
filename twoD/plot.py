from constants import *
from computations import *
from fileWriter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Global variable to store all the data
F = []          # 3 dimensional



# Loading the data into the variable F
def loadData(filename):
    print 'Loading the data ...'
    mat = []        # 2 dim
    with open(filename + '.txt', 'r') as f:
        for line in f:
            if line != '\n':
                row = map(float, line.split())
                mat.append(row)
            else:
                F.append(mat)
                #print 'norm stuff... ' + str(sum(array(mat)) / sum(array(F[0])))
                mat = []
        F.append(mat)



# Plot just the potential V
def plotPot(V):
    fig = plt.figure()
    im = plt.imshow(V, animated=True)
    plt.colorbar(im)
    show()




# Make a color plot of the data in F.
# NOTE: the data has to be parsed to F beforehand.
# The argument filename is the name of the outputted video, this part is still
# under construction
def plotColor(filename):
    fig = plt.figure(figsize=(10,20))
    plt.xlabel('$ x $')
    plt.ylabel('$ y $')
    z = F[0]
    im = plt.imshow(z, animated=True)
    plt.clim(0,0.5)
    plt.colorbar(im, label='wave function probability $ \parallel \psi ( x, y ) \parallel  ^ 2 $ ')


    def updatefig(i):
        try:
            im.set_array(F[i])
        except TypeError:
            quit()
        return im,

    # UNDER CONSTRUCTION
    # Set up formatting for the movie files
    #Writer = animation.writers['mencoder']
    #writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)

    ani = animation.FuncAnimation(fig, updatefig, interval=speed, blit=True)
    # UNDER CONSTRUCTION
    #ani.save(filename + '.mp4', writer=writer)
    show()




# Make a 3D plot of the data in F. This method of plotting it is slower than the
# color plot method!
# NOTE: the data has to be parsed to F beforehand.
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

