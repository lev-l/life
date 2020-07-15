from tkinter import *
from random import randint
from threading import Timer

#width and height of window
w = 10
h = 10
#create window
tk = Tk()
win = Canvas(tk, width=w * 50, height=h * 50)
#create list of cells
cells = [1] * w
for i in range(0, w):
    cells[i] = [0] * h

for i in range(0, w):
    for i1 in range(0, h):
        cells[i][i1] = randint(0, 1)
    i1 = 0

class ENGINE(object):
    """class for the main logic"""
    def __init__(self, cells, w, h):
        #the variable where we look at the cell map
        self.cells = cells
        #variable where we put new cell values
        self.new_cells = cells
        #see the width
        self.w = w
        #see the height
        self.h = h
        #number of neigbors
        self.neig = 0
        #start x
        self.sx = 0
        #start y
        self.sy = 0

    def repaint(self):
        """paint cells from the cell's list"""
        global win
        x = self.sx
        y = self.sy
        #clear the window
        win.delete(ALL)
        #main loop for paint cells
        for x, non in enumerate(self.cells):
            for y, non in enumerate(self.cells[x]):
                if self.cells[x][y] == 1:
                    win.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="green")
            y = 0
        win.pack()

    def DoSoN(self, present):  # Die or Sex or None
        #rules of the game named "life"
        if self.neig < 2:
            return 0
        elif self.neig > 3:
            return 0
        elif self.neig == 2:
            #the present value of cell
            return present
        else:
            return 1

    def neighbors(self):
        """look for neigbors of this cell"""
        x = self.sx - 1
        y = self.sy - 1
        self.neig = 0
        #look for neigbors(like in "sapper")
        while x < self.sx + 2:
            while y < self.sy + 2:
                #not go beyond
                if x >= 0 and x < self.w and 0 <= y < self.h:
                    if self.cells[x][y] == 1:
                        #do not take the value of the cell for which we are looking for neighbors
                        if not x == self.sx or not y == self.sy:
                            self.neig += 1
                y += 1
            y = self.sy - 1
            x += 1
        #does this cell die or alife
        dsn = self.DoSoN(self.cells[self.sx][self.sy])
        self.new_cells[self.sx][self.sy] = dsn
        self.neig = 0

    def life(self):
        """main loop"""
        #look for neigbors for all cells
        for self.sx, non in enumerate(self.cells):
            for self.sy, non in enumerate(self.cells[self.sx]):
                self.neighbors()
            self.sy = 0
        self.sx = 0
        self.sy = 0
        #upgrade cells map
        self.cells = self.new_cells
        if __name__ == '__main__':
            #start main loop
            self.repaint()
            Timer(0.1, self.life).start()
        else:
            #if this script run from tests, do not start main loop, but return the cells map
            return self.cells

#start
en = ENGINE(cells, w, h)
if __name__ == '__main__':
    en.life()
    win.mainloop()
