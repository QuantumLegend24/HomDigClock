from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

root = Tk()
root.title("Big Ben")
root.config(bg="white")

mytimeclocktimeclock_label = Label(root, font=("calibri", 100, "bold"), background="black", foreground="white")
mytimeclocktimeclock_label.pack(anchor="center")



colors = ["red", "green", "blue", "yellow", "purple", "orange", "white", "cyan", "pink"]
bg_color = random.choice(colors)
fg_color = random.choice(colors)
    
    
while bg_color == fg_color:
    fg_color = random.choice(colors)
    
mytimeclocktimeclock_label.config(background=bg_color, foreground=fg_color)

def time():
    string = strftime("%H:%M:%S %p")
    mytimeclocktimeclock_label.config(text=string)
    mytimeclocktimeclock_label.after(1000, time)


time()


root.mainloop()