from tkinter import *
import time
import random
from blocks import *

WIDTH = 500
HEIGHT = 600

color_list = ['red', 'blue', 'yellow', 'green', 'pink', 'orange']
random_color = random.choice(color_list)


def new_instance():
    window = Tk()
    window.title("Tetrisik")

    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#B672D8")
    canvas.pack()

    z_block = ZBlock(window, canvas, random_color)

    while True:
        z_block.fall()
        window.update()
        time.sleep(0.1)

    window.mainloop()
