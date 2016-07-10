from pylab import *

from constants import *
from computations import *
from fileWriter import *
from plot import *



def doComputations(filename):

    '''
    Setup all the stuff

    possible initial functions and potential combinations
        
        f_ini = gauss(4,3,1,0)
        V: harmonicPot
        -> harmonic2.txt


        f_ini = 2* gauss(4,0,-4,0)
        V_xy = gauss(0,0,0,0) ** 2
        -> singleScatter1.txt
        hbar = .1
        m = 1.
        speed = 200

        dx = 0.1
        dy = 0.1
        dt = 0.05


        N=500
        time = arange(0,N*dt,dt)

        L_x = 20.
        L_y = 10.

        f_ini = gauss(4,3,1,0)
        quarticPot
        -> quartic4.txt
        1, 0.1, 10


    '''
    print "Computation started ...\n"
    f_ini = laguerre()
    Norm = sum(abs(f_ini)**2) * dx * dy
    V_xy = zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(x)):
            V_xy[i,j] = centralPot(x[i], y[j])
    print "Potential initialized."
    
        


    '''
    Do the time stepping
    '''
    delete(filename)
    a1=f_ini
    for i in range(N):
        a2=nlStep(a1,V_xy,i)
        a3=fStep(a2)
        a1=a3
       # print 'norm stuff... ' + str(sum(abs(array(a3))**2) / sum(abs(array(f_ini))**2))
        saveMat(filename, abs(a1) ** 2)
        insertemptyLine(filename)
            


    print 'The data has been written to ' + filename
    

if __name__ == "__main__":
    doComputations(filename)
    loadData(filename)
    plotColor()
