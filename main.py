#export DISPLAY=:0.0
#size = 1024 x 600
#curl https://raw.githubusercontent.com/phuongnam0907/public_data/setup/script/setup_port.sh | bash
import serial as serial

from Utilities import modbus485

print("Hello BK Innovation Demo")

import time
import tkinter as tk
from tkinter import *
from mqtt import *
from Utilities.softwaretimer import *
from Utilities.modbus485 import *
import Utilities.modbus485

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
m485 = Utilities.modbus485.Modbus485(ser)

window = tk.Tk()

relay1_ON = [1, 6, 0, 0, 0, 255, 201, 138]
relay1_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

is_on = False
def toggle_button_click_1():
    global  is_on
    print("Button 1 is clicked")

    if is_on:
        on_button_v1.config(image=off)
        is_on = False
        m485.modbus485_send(relay1_OFF)
    else:
        on_button_v1.config(image=on)
        is_on = True
        m485.modbus485_send(relay1_ON)


    pass
def toggle_button_click_1():
    print("Button 2 is clicked")
    #m485.modbus485_send(relay1_OFF)
    pass



#window.attributes('-fullscreen', True)
window.geometry("1024x600")
window.title("Rapido Project")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)

on = PhotoImage(file="Images/on_button.png")
off = PhotoImage(file="Images/off_button.png")
on_button_v1 = Button(window, image=on, bd=0, command=toggle_button_click_1, justify=CENTER)
on_button_v2 = Button(window, image=on, bd=0, command=toggle_button_click_2, justify=CENTER)
on_button_v1.place(x=100, y=100, width=500)
on_button_v1.place(x=200, y=100, width=500)

while True:
    window.update()
    time.sleep(0.1)