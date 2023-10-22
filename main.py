#export DISPLAY=:0.0
#size = 1024 x 600
print("Hello BK Innovation Demo")

import time

import tkinter as tk
from tkinter import *
from mqtt import *
window = tk.Tk()

window.attributes('-fullscreen', True)
window.title("Rapido Project")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)


while True:
    window.update()
    time.sleep(0.1)