from tkinter import Tk
from tkinter import Label
import time


root =  Tk()
root.title('Display Clock')

def time_display():
    display_time = time.strftime('%H:%M:%S %p')
    clock.config(text = display_time)
    clock.after(180, time_display)
clock = Label(root, font= ('impact', 16), bg= 'blue',fg = 'red')
clock.pack()
time_display()
root.mainloop()