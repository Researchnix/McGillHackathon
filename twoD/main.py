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


    '''
    print "Computation started ...\n"
    f_ini = gauss(4,3,1,0)
    V_xy = zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(x)):
            V_xy[i,j] = quarticPot(x[i], y[j])
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
        saveMat(filename, abs(a1) ** 2)
        insertemptyLine(filename)

    print 'The data has been written to ' + filename
    

if __name__ == "__main__":
    #doComputations(filename)
    loadData(filename)
    plotColor()
