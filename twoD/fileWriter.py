'''
File writer to save results in the computation
'''
import os
from numpy import *


'''
Deleting a file

Args:   filename : string
'''
def delete(filename):
    try:
        os.remove(filename + '.txt')
    except OSError:
        pass


def insertemptyLine(filename):
    f = open(filename + '.txt', 'a')
    f.write('\n')
    f.close()
    

def saveMat(filename, mat):
    for row in mat:
        saveRow(filename + '.txt', row)
        

'''
Args:   filename : string
        row : array
'''
def saveRow(filename, row):
    f = open(filename + '.txt', 'a')
    f.write(convert(row) + '\n')
    f.close()


'''
Args:   filename : string
'''
def read(filename):
    with open(filename + '.txt', 'r') as f:
        for line in f:
            print line.split()
    f.close()



def convert(row):
    string = ''
    for e in row:
        string += str(e)
        string += ' '
    return string
