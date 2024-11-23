# def is_prime(number):
#     res = "prime"
#     for i in range(2,number):
#         if number % i == 0:
#             res = "not prime"
#             break
#     return res

# for i in range(2,100):
#     print(f"{i} is {is_prime(i)}")


    
# import tkinter

# root = tkinter.Tk()
# root.title("myapp")
# root.geometry("400x300")


# e1 = tkinter.Entry(root, border=15, highlightthickness=2, highlightcolor="red", highlightbackground="green")
# e1.pack()

# root.mainloop()


# import tkinter as tk

# def my_function():
#     output.config(text=my_variable.get())

# root = tk.Tk()

# output = tk.Label(root)
# output.pack()
# my_variable = tk.StringVar()
# r1 = tk.Radiobutton(root, text="football", value="football", command=my_function, variable=my_variable)
# r1.pack(anchor="w")
# r2 = tk.Radiobutton(root, text="basketball", value="basketball", command=my_function, variable=my_variable)
# r2.pack(anchor="w")
# root.mainloop()


import tkinter as tk

root = tk.Tk()
main_menu = tk.Menu(root)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
main_menu.add_cascade(label="File", menu=file_menu)
root.config(menu=main_menu)
root.mainloop()