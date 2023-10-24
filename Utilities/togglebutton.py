from tkinter import *
class ToggleButton:
    is_on = False
    on = NONE
    off = NONE
    on_click_event = NONE
    on_button = NONE

    def toggle_button_click(self):
        if self.is_on:
            self.on_button.config(image=self.off)
            self.is_on = False

        else:
            self.on_button.config(image=self.on)
            self.is_on = True

        self.on_click_event(self.is_on)
    
    def update_button_click(self, state):
        self.is_on = state
        if self.is_on:
            self.on_button.config(image=self.on)
            self.is_on = True
        else:
            self.on_button.config(image=self.off)
            self.is_on = False

    def __init__(self, win):
        # self.on = PhotoImage(file="E:/Documents/Thesis Proposal/BKInnovationDemo/Images/on_button_m.png")
        # self.off = PhotoImage(file="E:/Documents/Thesis Proposal/BKInnovationDemo/Images/off_button_m.png")
        self.on = PhotoImage(file="Images/on_button_m.png")
        self.off = PhotoImage(file="Images/off_button_m.png")

        self.is_on = False
        self.on_button = Button(win, image=self.off, bd=0, command=self.toggle_button_click, justify=CENTER)

    def setClickEvent(self, func):
        self.on_click_event = func

    def button_place(self, x_coor, y_coor):
        self.on_button.place(x = x_coor, y = y_coor)