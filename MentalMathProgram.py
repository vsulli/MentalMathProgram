# Mental Math Program
# graphical program to perform addition, subtraction, 
# multiplication, division and keep track of time taken to solve
# 13 December 2023

import tkinter as tk

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        self.root.mainloop()

    def show_message(self):
        print("Hello World")

MyGUI()

# menu
# digits of 1st num, digits of 2nd num

# addition
# subtraction
# multiplication
# division

