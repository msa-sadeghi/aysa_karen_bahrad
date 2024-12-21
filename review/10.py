from PIL import Image, ImageTk
from tkinter import Tk, Label, PhotoImage
import tkinter.font as font
import pyglet
# tkextrafont
window = Tk()

font.nametofont("TkDefaultFont").configure(family="BAUHS93.TTF", size=15)
pyglet.font.add_file("file.ttf")
# first method
# img_tk = ImageTk.PhotoImage(Image.open("user.png"))
# Label(window, text="username", image=img_tk, compound="left").pack()
# second method
img_tk = PhotoImage(file="user.png")
Label(window, text="username", image=img_tk,
      compound="left", font=("font name")).pack()

window.mainloop()
