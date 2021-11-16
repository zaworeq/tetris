from tkinter import *

class Block:

    def __init__(self,canvas,x,y,width, height,color):
        self.canvas = canvas
        x2 = x + width
        y2 = y+height
        self.image = canvas.create_rectangle(x,y,x2,y2,fill=color)

    def smth(self):
        pass
