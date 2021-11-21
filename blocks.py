from tkinter import *
from PIL import Image
import time

SPAWNX = 235
SPAWNY = 30
SPAWNVELOCITY = 10


class ZBlock:

    def __init__(self, window, canvas, color):
        self.canvas = canvas
        self.window = window
        self.color = color
        self.state = "horizontal"
        self.image = canvas.create_polygon(SPAWNX, SPAWNY,
                                            SPAWNX, SPAWNY + 10,
                                            SPAWNX - 10, SPAWNY + 10,
                                            SPAWNX - 10, SPAWNY + 20,
                                            SPAWNX + 10, SPAWNY + 20,
                                            SPAWNX + 10, SPAWNY + 10,
                                            SPAWNX + 20, SPAWNY + 10,
                                            SPAWNX + 20, SPAWNY,
                                            fill=self.color)

    def move_left(self, event):
        coordinates = self.canvas.coords(self.image)
        if (coordinates[0] <= (self.canvas.winfo_width()) and coordinates[0] > 15):
            self.canvas.move(self.image, -10, 0)
        else:
            self.window.bind("<Right>", self.move_right)

    def move_right(self, event):
        coordinates = self.canvas.coords(self.image)
        if (coordinates[0] < (self.canvas.winfo_width() - 30) and coordinates[0] >= 0):
            self.canvas.move(self.image, +10, 0)
        elif(coordinates[0] < (self.canvas.winfo_width() - 20) and coordinates[0] >= 0 and self.state == "vertical"):
            self.canvas.move(self.image, +10, 0)
        else:
            self.window.bind("<Left>", self.move_left)

    def rotation(self, event):
        coordinates = self.canvas.coords(self.image)
        if(self.state == "horizontal"):
            self.canvas.delete(self.image)
            self.image = self.canvas.create_polygon(coordinates[0], coordinates[1],
                                                coordinates[2], coordinates[3] - 20,
                                                coordinates[4], coordinates[5] - 20,
                                                coordinates[6], coordinates[7] - 10,
                                                coordinates[8] - 10, coordinates[9] - 10,
                                                coordinates[10] - 10, coordinates[11] + 10,
                                                coordinates[12] - 10, coordinates[13] + 10,
                                                coordinates[14] - 10, coordinates[15],
                                                fill=self.color)
            self.state = "vertical"
        elif(self.state == "vertical" and coordinates[0] <= (self.canvas.winfo_width() - 15) and coordinates[0] > (self.canvas.winfo_width() - 25)):
            print(coordinates)
            self.canvas.move(self.image, -10, 0)
            self.canvas.delete(self.image)
            self.image = self.canvas.create_polygon(coordinates[0] - 10, coordinates[1],
                                                    coordinates[2] - 10, coordinates[3] + 20,
                                                    coordinates[4] - 10, coordinates[5] + 20,
                                                    coordinates[6] - 10, coordinates[7] + 10,
                                                    coordinates[8], coordinates[9] + 10,
                                                    coordinates[10], coordinates[11] - 10,
                                                    coordinates[12], coordinates[13] - 10,
                                                    coordinates[14], coordinates[15],
                                                    fill=self.color)
            self.state = "horizontal"
        else:
            self.canvas.delete(self.image)
            self.image = self.canvas.create_polygon(coordinates[0], coordinates[1],
                                                    coordinates[2], coordinates[3] + 20,
                                                    coordinates[4], coordinates[5] + 20,
                                                    coordinates[6], coordinates[7] + 10,
                                                    coordinates[8] + 10, coordinates[9] + 10,
                                                    coordinates[10] + 10, coordinates[11] - 10,
                                                    coordinates[12] + 10, coordinates[13] - 10,
                                                    coordinates[14] + 10, coordinates[15],
                                                    fill=self.color)
            self.state = "horizontal"

    def fall(self):
        coordinates = self.canvas.coords(self.image)
        if(coordinates[9]>=(self.canvas.winfo_height() - 10) and self.state == "horizontal"):
            return False
        elif(coordinates[11]>=(self.canvas.winfo_height() - 10) and self.state == "vertical"):
            return False
        self.canvas.move(self.image, 0, SPAWNVELOCITY)

        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<Up>", self.rotation)
