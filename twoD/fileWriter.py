'''
    File writer to save results of the computations
'''
import os
from numpy import *


'''
    Deleting the file if it exists, if an exception is thrown, ignore it

    Args:   filename : string
'''
def delete(filename):
    try:
        os.remove(filename + '.txt')
    except OSError:
        pass

'''
    Inserting an empty line in the file
'''
def insertemptyLine(filename):
    f = open(filename + '.txt', 'a')
    f.write('\n')
    f.close()
    
'''
    Writing an entire 2D array to the file
'''
def saveMat(filename, mat):
    for row in mat:
        saveRow(filename, row)
        

'''
    Saving just a row of a 2D array, i.e simply an array to the file
    Args:   filename : string
        row : array
'''
def saveRow(filename, row):
    f = open(filename + '.txt', 'a')
    f.write(convert(row) + '\n')
    f.close()


'''
    Reading and printing the entire file for debugging purposes 
    Args:   filename : string
'''
def read(filename):
    with open(filename + '.txt', 'r') as f:
        for line in f:
            print line.split()
    f.close()


'''
    conerting an array to a string where every element in the array is separated
    by a space
'''
def convert(row):
    string = ''
    for e in row:
        string += str(e)
        string += ' '
    return string
