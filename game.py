from tkinter import *
import time
from blocks import *

WIDTH = 500
HEIGHT = 600


def new_instance():
    window = Tk()
    window.title("Tetrisik")

    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#B672D8")
    canvas.pack()

    blue_s_block = SBlock(window, canvas, "blue")

    while True:
        blue_s_block.fall()
        window.update()
        time.sleep(0.1)

    window.mainloop()
