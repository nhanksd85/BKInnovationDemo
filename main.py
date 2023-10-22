#export DISPLAY=:0.0
#size = 1024 x 600
#curl https://raw.githubusercontent.com/phuongnam0907/public_data/setup/script/setup_port.sh | bash
print("Hello BK Innovation Demo")

import time
import tkinter as tk
from tkinter import *
from mqtt import *
window = tk.Tk()

def toggle_button_click():
    pass

#window.attributes('-fullscreen', True)
window.geometry("1024x600")
window.title("Rapido Project")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)

on = PhotoImage(file="Images/on_button.png")
off = PhotoImage(file="Images/off_button.png")
on_button = Button(window, image=on, bd=0, command=toggle_button_click, justify=CENTER)

on_button.place(x=100, y=100, width=500)

while True:
    window.update()
    time.sleep(0.1)