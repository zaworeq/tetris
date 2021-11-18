from tkinter import *
from PIL import Image
import time

SPAWNX = 237
SPAWNY = 30
SPAWNVELOCITY = 10


class SBlock:

    def __init__(self, window, canvas, color):
        self.canvas = canvas
        self.window = window
        self.image = canvas.create_polygon(SPAWNX, SPAWNY,
                                            SPAWNX, SPAWNY + 10,
                                            SPAWNX - 10, SPAWNY + 10,
                                            SPAWNX - 10, SPAWNY + 20,
                                            SPAWNX + 10, SPAWNY + 20,
                                            SPAWNX + 10, SPAWNY + 10,
                                            SPAWNX + 20, SPAWNY + 10,
                                            SPAWNX + 20, SPAWNY,
                                            fill=color)

    def move_left(self, event):
        self.canvas.move(self.image, -10, 0)

    def move_right(self, event):
        self.canvas.move(self.image, +10, 0)

    def rotation(self, event):
        coordinates = self.canvas.coords(self.image)
        print(coordinates)

    def fall(self):
        coordinates = self.canvas.coords(self.image)
        if(coordinates[3]>=(self.canvas.winfo_height() - 20) or coordinates[1]<0):
            return False
        self.canvas.move(self.image, 0, SPAWNVELOCITY)

        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<Up>", self.rotation)
