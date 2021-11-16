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

    blue_block = Block(canvas, 237, 0, 10, 10, "blue")

    window.mainloop()
