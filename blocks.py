from tkinter import *
from PIL import Image
import time

SPAWNX = 237
SPAWNY = 30
SPAWNVELOCITY = 10


class Block:

    def __init__(self, window, canvas, x, y, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, y_velocity, color):
        self.canvas = canvas
        self.window = window
        self.image = canvas.create_polygon(x, y, x2, y2, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, fill=color)
        self.y_velocity = y_velocity

    def move_left(self, event):
        self.canvas.move(self.image, -10, 0)

    def move_right(self, event):
        self.canvas.move(self.image, +10, 0)

    def rotation(self, event):
        pass

    def fall(self,):
        coordinates = self.canvas.coords(self.image)
        # print(coordinates)
        if(coordinates[3]>=(self.canvas.winfo_height() - 20) or coordinates[1]<0):
            return False
        self.canvas.move(self.image, 0, self.y_velocity)

        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<Up>", self.rotation)


class SBlock(Block):

    def __init__(self, window, canvas, color):
        self.canvas = canvas
        self.window = window
        self.block1 = Block(window,
                            canvas,
                            SPAWNX, SPAWNY,
                            SPAWNX, SPAWNY + 10,
                            SPAWNX - 10, SPAWNY + 10,
                            SPAWNX - 10, SPAWNY + 20,
                            SPAWNX + 10, SPAWNY + 20,
                            SPAWNX + 10, SPAWNY + 10,
                            SPAWNX + 20, SPAWNY + 10,
                            SPAWNX + 20, SPAWNY,
                            SPAWNVELOCITY, color)

        while True:
            self.block1.fall()
            window.update()
            time.sleep(0.1)