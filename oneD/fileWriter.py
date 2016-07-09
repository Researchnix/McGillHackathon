'''
File writer to save results in the computation
'''
import os


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


filename = "text.txt"
delete(filename)
save(filename, "hello test")
save(filename, "another line")
read(filename)





