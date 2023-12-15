# Mental Math Program
# graphical program to perform addition, subtraction, 
# multiplication, division and keep track of time taken to solve
# 13 December 2023

import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Mental Math Program")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack()
root.mainloop()

# menu
# digits of 1st num, digits of 2nd num

# addition
# subtraction
# multiplication
# division

