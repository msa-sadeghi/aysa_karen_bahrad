from PIL import Image, ImageTk
from tkinter import Tk, Label



window = Tk()


img_tk = ImageTk.PhotoImage(Image.open("user.png"))
Label(window, text="username", image=img_tk, compound="left").pack()
window.mainloop()
