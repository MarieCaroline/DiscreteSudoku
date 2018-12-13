# This is the naive sudoku generator.

# class that controls the content of each individual cell describing its location
# and properties on the grid
class Cell:
    def __init__(self, row, column, square, value):
        self.c = column
        self.r = row
        self.s = square
        self.v = value
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
    #square "math" applies the right square number to each cell
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
#row[0].v = 3 

# Display the starting grid.
for j in range(9):
    i = j*9
    print str(row[i].v) + str(row[i+1].v) + str(row[i+2].v) + str(row[i+3].v) + str(row[i+4].v) + str(row[i+5].v) + str(row[i+6].v) + str(row[i+7].v) + str(row[i+8].v)

# start inserting numbers
i = 0
while i < len(row):
    cond = True
    while cond:
        cond = False
        while row[i].v == 9: #if value is 9 (and thus it has tried all numbers) go back to the previous cell
            row[i].v = 0
            i = i - 1    
        row[i].v = row[i].v + 1 # increase current cell by 1
        for l in range(len(row)): # make sure the current int is not the same as any in its row, column, or square
            if row[i].r == row[l].r or row[i].c == row[l].c or row[i].s == row[l].s:
                if i == l: # ignore "conflict" if comparing to itself
                    pass
                elif row[i].v == row[l].v:
                    cond = True # if there is a conflict try changing the value again
    i = i + 1 # go to next cell

# display resulting sudoku grid
i = 0
for j in range(9):
    i = j*9
    print str(row[i].v) + str(row[i+1].v) + str(row[i+2].v) + '|' + str(row[i+3].v) + str(row[i+4].v) + str(row[i+5].v) + '|' + str(row[i+6].v) + str(row[i+7].v) + str(row[i+8].v)
    if j == 2 or j == 5:
        print '-----------'
