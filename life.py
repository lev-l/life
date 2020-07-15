from tkinter import *
from random import randint
from threading import Timer

w = 10
h = 10
tk = Tk()
win = Canvas(tk, width=w * 50, height=h * 50)
cells = [1] * w
for i in range(0, w):
    cells[i] = [0] * h

for i in range(0, w):
    for i1 in range(0, h):
        cells[i][i1] = randint(0, 1)
    i1 = 0

class ENGINE(object):

    def __init__(self, cells, w, h):
        self.cells = cells
        self.new_cells = cells
        self.w = w
        self.h = h
        self.neig = 0
        self.sx = 0
        self.sy = 0

    def repaint(self):
        global win
        x = self.sx
        y = self.sy
        win.delete(ALL)
        for x, non in enumerate(self.cells):
            for y, non in enumerate(self.cells[x]):
                if self.cells[x][y] == 1:
                    win.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="green")
            y = 0
        win.pack()

    def DoSoN(self, present):  # Die or Sex or None
        if self.neig < 2:
            return 0
        elif self.neig > 3:
            return 0
        elif self.neig == 2:
            return present
        else:
            return 1

    def neighbors(self):
        x = self.sx - 1
        y = self.sy - 1
        self.neig = 0
        while x < self.sx + 2:
            while y < self.sy + 2:
                if x >= 0 and x < self.w and 0 <= y < self.h:
                    if self.cells[x][y] == 1:
                        if not x == self.sx or not y == self.sy:
                            self.neig += 1
                y += 1
            y = self.sy - 1
            x += 1
        dsn = self.DoSoN(self.cells[self.sx][self.sy])
        self.new_cells[self.sx][self.sy] = dsn
        self.neig = 0

    def life(self):
        for self.sx, non in enumerate(self.cells):
            for self.sy, non in enumerate(self.cells[self.sx]):
                self.neighbors()
            self.sy = 0
        self.sx = 0
        self.sy = 0
        self.cells = self.new_cells
        if __name__ == '__main__':
            self.repaint()
            Timer(0.1, self.life).start()
        else:
            return self.cells


en = ENGINE(cells, w, h)
if __name__ == '__main__':
    en.life()
    win.mainloop()
