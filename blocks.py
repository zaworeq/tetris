from tkinter import *

SPAWNX = 237
SPAWNY = 20
SPAWNVELOCITY = 10


class Block:

    def __init__(self, canvas, x, y, width, height, y_velocity, color):
        self.canvas = canvas
        x2 = x + width
        y2 = y+height
        self.image = canvas.create_rectangle(x, y, x2, y2, fill=color)
        self.y_velocity = y_velocity

    def fall(self):
        coordinates = self.canvas.coords(self.image)
        # print(coordinates)
        if(coordinates[3]>=(self.canvas.winfo_height() - 10) or coordinates[1]<0):
            return False
        self.canvas.move(self.image, 0, self.y_velocity)


class SBlock(Block):

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.block1 = Block(canvas, SPAWNX, SPAWNY, 10, 20, SPAWNVELOCITY, color)
        self.block2 = Block(canvas, SPAWNX - 10, SPAWNY + 10, 10, 20, SPAWNVELOCITY, color)

    def s_fall(self):
        self.block1.fall()
        self.block2.fall()
