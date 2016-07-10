from pylab import *
from constants import *
from computations import *
from fileWriter import *
from plot import *


# Main method for the computations which sets up the potential V_xy and the
# inital wave function f_ini and runs the time stepping.
# All parameters are set in the constant.py file
# The resulting data is stored in the file "filename.txt"
def doComputations(filename):
    '''
    Setup
    '''
    print "Computation started ..."
    # The initial function for the time stepping
    f_ini = laguerre(0.,-1.5)
    # Only compute the norm to check if the time stepping is not losing any
    # probability
    # Norm = sum(abs(f_ini)**2) * dx * dy
    # Initialize the potential
    # Choose from the different potentials in computations.py
    V_xy = zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(x)):
            V_xy[i,j] = centralPot(x[i]-1.5, y[j])+centralPot(x[i]+1.5, y[j])
    print "Potential initialized ..."
    
        


    '''
    Do the time stepping
    '''
    # Delete the file if it exists
    delete(filename)
    a1=f_ini
    # Propagate the time dependend Schroedinger equation by turns 
    # by a nonlinear Step and by linear Step in the fourier space and write the
    # intermediate results to a file using our fileWriter.py
    for i in range(N):
        a2=nlStep(a1,V_xy,i)
        a3=fStep(a2)
        a1=a3
        # Again a way to double check if the normalization stays constant while
        # propagating in time
        #print 'norm stuff... ' + str(sum(abs(array(a3))**2) 
        #/ sum(abs(array(f_ini))**2))
        saveMat(filename, abs(a1) ** 2)
        insertemptyLine(filename)
   p rint 'The data has been written to ' + filename + '.txt'
    

if __name__ == "__main__":
    '''
    Uncomment any of the following commands to do the computations 
    or/and (only) load the data already in a txt file.
    plotPot plots a given potential, note to define it locally in the man
    function
    '''
    #doComputations(filename)
    loadData(filename)
    #dummy = raw_input("Ready when you are ...")
    plotColor(filename)
   # V_xy = easyGauss() 
    #plotPot(V_xy)
