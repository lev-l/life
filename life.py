from tkinter import *
from random import randint
from threading import Timer

w = 10
h = 10
tk = Tk()
win = Canvas(tk, width=w * 50, height=h * 50)
cells = [1] * w
i = 0
while i < w:
    cells[i] = [0] * h
    i += 1

i = 0
i1 = 0
while i < w:
    while i1 < h:
        cells[i][i1] = randint(0, 1)
        i1 += 1
    i1 = 0
    i += 1

class ENGINE(object):

    def __init__(self, cells, w, h):
        self.cells = cells
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
        while x < self.w:
            while y < self.h:
                if self.cells[x][y] == 1:
                    win.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="green")
                y += 1
            y = 0
            x += 1
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
        self.cells[self.sx][self.sy] = dsn
        self.neig = 0

    def life(self):
        while self.sx < self.w:
            while self.sy < self.h:
                self.neighbors()
                self.sy += 1
            self.sx += 1
            self.sy = 0
        self.sx = 0
        self.sy = 0
        self.repaint()
        Timer(0.1, self.life).start()


en = ENGINE(cells, w, h)
en.life()
win.mainloop()
