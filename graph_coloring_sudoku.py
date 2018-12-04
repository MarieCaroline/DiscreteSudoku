from random import shuffle, sample
import numpy as np


# class that controls the content of each individual cell describing its location
# and properties on the grid
class Cell:
    def __init__(self, row, column, square, value):
        self.c = column
        self.r = row
        self.s = square
        self.v = value
        self.n = range(1,10)
        self.e = True
# generation of an empty 9x9 grid of cells with the correct properties for each cell
row = []
x = 0
for i in range(81):
    #row math
    r = (i+9)/9
    #column math
    c = i + 1 - x
    if c == 9:
        x = x + 9
    #square "math"
    if r == 1 or r == 2 or r == 3:
        if c == 1 or c == 2 or c == 3:
            s = 1
        elif c == 4 or c == 5 or c == 6:
            s = 2
        elif c == 7 or c == 8 or c == 9:
            s = 3
    elif r == 4 or r == 5 or r == 6:
        if c == 1 or c == 2 or c == 3:
            s = 4
        elif c == 4 or c == 5 or c == 6:
            s = 5
        elif c == 7 or c == 8 or c == 9:
            s = 6
    elif r == 7 or r == 8 or r == 9:
        if c == 1 or c == 2 or c == 3:
            s = 7
        elif c == 4 or c == 5 or c == 6:
            s = 8
        elif c == 7 or c == 8 or c == 9:
            s = 9
    v = 0
    row.append(Cell(r,c,s,v))

# Change this to force the first cell to start searching at a certain value
# This could be done for any or multiple cells. It does not guarantee that cell will...
# contain that value.
# row[0].v = 0

#shuffles the order of row so that the cells aren't analyzed in 1-81 order
# shuffle(row)
# row[1].v = 1
# row[2].v = 2
# row[3].v = 3
# row[4].v = 4
# row[5].v = 5
# row[6].v = 6
# row[7].v = 7
# row[8].v = 8


# Display the starting grid.
for j in range(9):
    i = j*9
    print str(row[i].v) + str(row[i+1].v) + str(row[i+2].v) + str(row[i+3].v) + str(row[i+4].v) + str(row[i+5].v) + str(row[i+6].v) + str(row[i+7].v) + str(row[i+8].v)
highi = 0
# start inserting numbers
i = 0
while i < len(row):
    cond = True
    while cond:
        cond = False
        # while row[i].v == 9: #if value is 9 (and thus it has tried all numbers) go back to the previous cell
        #     row[i].v = 0
        #print i
        while row[i].n == []:
            row[i].v = 0
            row[i].n = range(1,10)
            i = i - 1    
        #row[i].v = row[i].v + 1 # increase current cell by 1
        rlist = row[i].n
        #print rlist
        random = sample(rlist, 1)
        #print random
        row[i].v = random[0]
        rlist.remove(random[0])
        row[i].n = rlist
        #print rlist
        for l in range(len(row)): # make sure the current int is not the same as any in its row, column, or square
            if row[i].r == row[l].r or row[i].c == row[l].c or row[i].s == row[l].s:
                
                #print "cell:" + str(i) + 'compare' 
                if i == l: # ignore "conflict" if comparing to itself
                    pass
                elif row[i].v == row[l].v:
                    cond = True # if there is a conflict try changing the value again
                    #print 'conflict'
    i = i + 1 # go to next cell

i = 0
#row = unshuffle
for j in range(9):
    i = j*9
    print str(row[i].v) + str(row[i+1].v) + str(row[i+2].v) + '|' + str(row[i+3].v) + str(row[i+4].v) + str(row[i+5].v) + '|' + str(row[i+6].v) + str(row[i+7].v) + str(row[i+8].v)
    if j == 2 or j == 5:
        print '-----------'

def make_array_from_class(row):
    a_list = []
    count = 0
    b_list = []
    for i in row:
        b_list.append(i.v)
        count = count + 1
        if count == 9:
            count = 0
            a_list.append(b_list)
            b_list = []
    return a_list

print make_array_from_class(row)

start = np.array(make_array_from_class(row), np.int8)

def random_variable()
    rownumber = sample(range(1,10),1)
    columnnumber = sample(range(1,10),1)
    return [rownumber, columnnumber]

thing = random_variable()










puzzle = np.array([[5,3,0, 0,7,0, 0,0,0],
                   [6,0,0, 1,9,5, 0,0,0],
                   [0,9,8, 0,0,0, 0,6,0],

                   [8,0,0, 0,6,0, 0,0,3],
                   [4,0,0, 8,0,3, 0,0,1],
                   [7,0,0, 0,2,0, 0,0,6],

                   [0,6,0, 0,0,0, 2,8,0],
                   [0,0,0, 4,1,9, 0,0,5],
                   [0,0,0, 0,8,0, 0,7,9]],np.int8)

