from tkinter import *
from PIL import Image, ImageTk
from game import new_instance


def new_game():
    menu.destroy()
    new_instance()


menu = Tk()
menu.title("Tetrisik")

canvas = Canvas(menu)
canvas.grid(row=0, column=0, rowspan=10, columnspan=11)

bg_image = ImageTk.PhotoImage(Image.open('menu_bg.jpg'))
menu_bg = canvas.create_image(0, 0, image=bg_image, anchor=NW)

start_btn = Button(menu, text="New game", font=("Times New Roman", 20), command=new_game)
start_btn.grid(row=8, column=5)

quit_btn = Button(menu, text="Quit", font=("Times New Roman", 20), command=quit)
quit_btn.grid(row=9, column=5)

menu.mainloop()
