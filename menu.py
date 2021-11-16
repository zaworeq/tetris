from tkinter import *
from game import new_instance


def new_game():
    menu.destroy()
    new_instance()


menu = Tk()
menu.title("Tetrisik")
menu.geometry("200x150")
menu.config(bg= "light green")

start_btn = Button(menu, text="New game", font=("Times New Roman",20), command= new_game)
start_btn.pack()

quit_btn = Button(menu, text="Quit", font=("Times New Roman",20), command= quit)
quit_btn.pack()

menu.mainloop()
