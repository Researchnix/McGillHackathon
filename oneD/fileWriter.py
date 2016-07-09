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
        os.remove(filename)
    except OSError:
        pass



'''
Args:   filename : string
        row : array
'''
def save(filename, row):
    f = open(filename, 'a')
    f.write(row + '\n')
    f.close()


'''
Args:   filename : string
'''
def read(filename):
    with open(filename, 'r') as f:
        for line in f:
            print line
    f.close()



def convert(myarray):
    out = ""
    for e in myarray:
        out += str(e)
        out += ','
    return out

"""

filename = "hello.txt"
delete(filename)
save(filename, "this is a line")
save(filename, "this is also a  line")
read(filename)

l = [1,2,3,4,5]
l1 = array(l)
print l1
print convert(l1)
save(filename, convert(l1))
read(filename)
"""
