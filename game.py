from tkinter import *
import time
import random
from blocks import *

WIDTH = 500
HEIGHT = 600


class Game:

    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.color_list = ['red', 'blue', 'yellow', 'green', 'pink', 'orange']
        self.random_color = random.choice(self.color_list)
        self.object_list = []

        for index in range(0, 10):
            index = ZBlock(self.window, self.canvas, self.random_color)
            self.object_list.append(index)

            while True:
                index.fall()
                window.update()
                time.sleep(0.1)


def new_instance():
    window = Tk()
    window.title("Tetrisik")

    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#B672D8")
    canvas.pack()

    game = Game(window, canvas)

    window.mainloop()
