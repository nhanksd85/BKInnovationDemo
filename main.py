#export DISPLAY=:0.0
#size = 1024 x 600
#curl https://raw.githubusercontent.com/phuongnam0907/public_data/setup/script/setup_port.sh | bash
import serial as serial

from Utilities import modbus485

print("Hello BK Innovation Demo")
import json
import time
import tkinter as tk
from tkinter import *

from Utilities.softwaretimer import *
from Utilities.modbus485 import *
import Utilities.modbus485
from Utilities.togglebutton import *
from mqtt import *
from Utilities.constant import *

def toggle_fullscreen(event = None):
    state = not window.attributes('-fullscreen')
    window.attributes('-fullscreen', state)
    
    if state:
        window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0")
    else:
        window.geometry("1024x600")  

# ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
try:
    ser = serial.Serial(port="COM7", baudrate=115200)
except:
    print("Modbus485**","Failed to write data")

m485 = Utilities.modbus485.Modbus485(ser)

window = tk.Tk()


def btn_valve_1_onClick(state):
    print("Button1 is click", state)
    if state:
        m485.modbus485_send(relay1_ON)
    else:
        m485.modbus485_send(relay1_OFF)
    pass

def btn_valve_2_onClick(state):
    print("Button2 is click", state)
    if state:
        m485.modbus485_send(relay2_ON)
    else:
        m485.modbus485_send(relay2_OFF)
    pass

def btn_valve_3_onClick(state):
    print("Button3 is click", state)
    if state:
        m485.modbus485_send(relay3_ON)
    else:
        m485.modbus485_send(relay3_OFF)
    pass

def btn_pump_flow_1_onClick(state):
    print("Flow 1 is click", state)
    if state:
        m485.modbus485_send(relay4_ON)
    else:
        m485.modbus485_send(relay4_OFF)
    pass

def btn_pump_flow_2_onClick(state):
    print("Flow 2 is click", state)
    if state:
        m485.modbus485_send(relay5_ON)
    else:
        m485.modbus485_send(relay5_OFF)
    pass

def btn_pump_flow_3_onClick(state):
    print("Flow 3 is click", state)
    if state:
        m485.modbus485_send(relay6_ON)
    else:
        m485.modbus485_send(relay6_OFF)
    pass

def btn_pump_1_onClick(state):
    print("Pump 1 is click", state)
    if state:
        m485.modbus485_send(relay7_ON)
    else:
        m485.modbus485_send(relay7_OFF)
    pass

def btn_pump_2_onClick(state):
    print("Pump 2 is click", state)
    if state:
        m485.modbus485_send(relay8_ON)
    else:
        m485.modbus485_send(relay8_OFF)
    pass


# Bind the F11 key to toggle full-screen
window.bind("<F11>", toggle_fullscreen)

# Bind the Escape key to exit full-screen
window.bind("<Escape>", toggle_fullscreen)

# Initial window size (optional)
window.attributes('-fullscreen', True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.wm_attributes("-topmost", 1)


window.title("Rapido Project")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)

####### SET VARIABLE

btn_var_1 = tk.BooleanVar()
btn_var_1.set(False)
btn_var_2 = tk.BooleanVar()
btn_var_2.set(False)
btn_var_3 = tk.BooleanVar()
btn_var_3.set(False)

btn_var1 = tk.BooleanVar()
btn_var1.set(False)
btn_var2 = tk.BooleanVar()
btn_var2.set(False)
btn_var3 = tk.BooleanVar()
btn_var3.set(False)
btn_var4 = tk.BooleanVar()
btn_var4.set(False)
btn_var5 = tk.BooleanVar()
btn_var5.set(False)

##### SOIL LABEL

labelSoil = tk.Label(text="SOIL STATION",fg="#ff0000",justify=CENTER,font="Helvetica 20 bold")
labelSoil.place(x=50, y=0, width=300, height=100)

labelSoil = tk.Label(text="TEMP (°C)",fg="#ff0000",justify=CENTER,font="Helvetica 15")
labelSoil.place(x=50, y=80, width=150, height=20)
labelSoil = tk.Label(text="HUMID (%)",fg="#ff0000",justify=CENTER,font="Helvetica 15")
labelSoil.place(x=200, y=80, width=150, height=20)

labelSoilTemp = tk.Label(text="35",fg="#ff0000",justify=CENTER,font="Helvetica 20 bold")
labelSoilTemp.place(x=50, y = 100, width=150)

labelSoilHumi = tk.Label(text="70",fg="#ff0000",justify=CENTER,font="Helvetica 20 bold")
labelSoilHumi.place(x=200, y = 100, width=150)

labelSoil = tk.Label(text="PH ()",fg="#ff0000",justify=CENTER,font="Helvetica 15")
labelSoil.place(x=50, y=150, width=150, height=20)
labelSoil = tk.Label(text="EC (ppm)",fg="#ff0000",justify=CENTER,font="Helvetica 15")
labelSoil.place(x=200, y=150, width=150, height=20)

labelSoilPH = tk.Label(text="5",fg="#ff0000",justify=CENTER,font="Helvetica 20 bold")
labelSoilPH.place(x=50, y = 170, width=150)

labelSoilEC = tk.Label(text="10",fg="#ff0000",justify=CENTER,font="Helvetica 20 bold")
labelSoilEC.place(x=200, y = 170, width=150)

labelSoil = tk.Label(text="N                 P                 K",fg="#ff0000",justify=CENTER,font="Helvetica 15")
labelSoil.place(x=50, y=220, width=300, height=20)

labelSoilN = tk.Label(text="10",fg="#ff0000",justify=CENTER,font="Helvetica 20 bold")
labelSoilN.place(x=35, y = 245, width=100)

labelSoilP = tk.Label(text="10",fg="#ff0000",justify=CENTER,font="Helvetica 20 bold")
labelSoilP.place(x=147, y = 245, width=100)

labelSoilK = tk.Label(text="10",fg="#ff0000",justify=CENTER,font="Helvetica 20 bold")
labelSoilK.place(x=263, y = 245, width=100)

##### AIR LABEL

labelAir = tk.Label(text="AIR STATION",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAir.place(x=350, y=0, width=300, height=100)

labelAir = tk.Label(text="TEMP (°C)",fg="#099940",justify=CENTER,font="Helvetica 15")
labelAir.place(x=350, y=80, width=150, height=20)
labelAir = tk.Label(text="HUMID (%)",fg="#099940",justify=CENTER,font="Helvetica 15")
labelAir.place(x=500, y=80, width=150, height=20)

labelAirTemp = tk.Label(text="335",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAirTemp.place(x=350, y = 100, width=150)

labelAirHumi = tk.Label(text="700",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAirHumi.place(x=500, y = 100, width=150)

labelAir = tk.Label(text="BRIGHT (Lux)",fg="#099940",justify=CENTER,font="Helvetica 15")
labelAir.place(x=350, y=150, width=150, height=20)
labelAir = tk.Label(text="PRESSURE (Kpa)",fg="#099940",justify=CENTER,font="Helvetica 15")
labelAir.place(x=495, y=150, width=160, height=20)

labelAirCO2 = tk.Label(text="5",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAirCO2.place(x=350, y = 170, width=150)

labelAirLux = tk.Label(text="10",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAirLux.place(x=500, y = 170, width=150)

##### WATER LABEL

labelWater = tk.Label(text="WATER STATION",fg="#0000ff",justify=CENTER,font="Helvetica 20 bold")
labelWater.place(x=700, y=0, width=300, height=100)

labelWater = tk.Label(text="TEMP (°C)",fg="#0000ff",justify=CENTER,font="Helvetica 15")
labelWater.place(x=700, y=80, width=150, height=20)
labelWater = tk.Label(text="PH ()",fg="#0000ff",justify=CENTER,font="Helvetica 15")
labelWater.place(x=850, y=80, width=150, height=20)

labelWaterTemp = tk.Label(text="3.35",fg="#0000ff",justify=CENTER,font="Helvetica 20 bold")
labelWaterTemp.place(x=700, y = 100, width=150)

labelWaterPH = tk.Label(text="7.00",fg="#0000ff",justify=CENTER,font="Helvetica 20 bold")
labelWaterPH.place(x=850, y = 100, width=150)


labelWater = tk.Label(text="EC (ppm)",fg="#0000ff",justify=CENTER,font="Helvetica 15")
labelWater.place(x=700, y=150, width=150, height=20)
labelWater = tk.Label(text="ORP (ppm)",fg="#0000ff",justify=CENTER,font="Helvetica 15")
labelWater.place(x=850, y=150, width=150, height=20)

labelWaterEC = tk.Label(text="5",fg="#0000ff",justify=CENTER,font="Helvetica 20 bold")
labelWaterEC.place(x=700, y = 170, width=150)

labelWaterORP = tk.Label(text="10",fg="#0000ff",justify=CENTER,font="Helvetica 20 bold")
labelWaterORP.place(x=850, y = 170, width=150)

##### FIRST GROUP BUTTON

labelMixNutriFood = tk.Label(text="TRỘN DINH DƯỠNG",
                                    fg="#0000ff",
                                    justify=CENTER,
                                    # bg = "#000",
                                    font="Helvetica 20 bold")

labelMixNutriFood.place(x=50, y=275, width=300, height=100)


labelNutriFood1 = tk.Label(text="DUNG DỊCH 1",fg="#0000ff",font="Helvetica 15 bold")
labelNutriFood1.place(x=50, y=370, width=200, height=50)
btn_valve_1 = ToggleButton(window)
btn_valve_1.setClickEvent(btn_valve_1_onClick)
btn_valve_1.button_place(250, 350)

labelNutriFood2 = tk.Label(text="DUNG DỊCH 2",fg="#0000ff",font="Helvetica 15 bold")
labelNutriFood2.place(x=50, y=445, width=200, height=50)
btn_valve_2 = ToggleButton(window)
btn_valve_2.setClickEvent(btn_valve_2_onClick)
btn_valve_2.button_place(250, 425)

labelNutriFood3 = tk.Label(text="DUNG DỊCH 3",fg="#0000ff",font="Helvetica 15 bold")
labelNutriFood3.place(x=50, y=520, width=200, height=50)

btn_valve_3 = ToggleButton(window)
btn_valve_3.setClickEvent(btn_valve_3_onClick)
btn_valve_3.button_place(250, 500)

##### SECOND GROUP BUTTON

labelRegion = tk.Label(text="PHÂN KHU TƯỚI",
                                    fg="#0000ff",
                                    justify=CENTER,
                                    # bg = "#000",
                                    font="Helvetica 20 bold")

labelRegion.place(x=350, y=275, width=300, height=100)

labelRegion1 = tk.Label(text="PHÂN KHU 1",fg="#0000ff",font="Helvetica 15 bold")
labelRegion1.place(x=350, y=370, width=200, height=50)

btn_pump_flow_1 = ToggleButton(window)
btn_pump_flow_1.setClickEvent(btn_pump_flow_1_onClick)
btn_pump_flow_1.button_place(550, 350)

labelRegion2 = tk.Label(text="PHÂN KHU 2",fg="#0000ff",font="Helvetica 15 bold")
labelRegion2.place(x=350, y=445, width=200, height=50)
btn_pump_flow_2 = ToggleButton(window)
btn_pump_flow_2.setClickEvent(btn_pump_flow_2_onClick)
btn_pump_flow_2.button_place(550, 425)

labelRegion3 = tk.Label(text="PHÂN KHU 3",fg="#0000ff",font="Helvetica 15 bold")
labelRegion3.place(x=350, y=520, width=200, height=50)
btn_pump_flow_3 = ToggleButton(window)
btn_pump_flow_3.setClickEvent(btn_pump_flow_3_onClick)
btn_pump_flow_3.button_place(550, 500)

##### THIRD GROUP BUTTON

labelPumps = tk.Label(text="MÁY BƠM CHÍNH",
                                    fg="#0000ff",
                                    justify=CENTER,
                                    # bg = "#000",
                                    font="Helvetica 20 bold")

labelPumps.place(x=700, y=275, width=300, height=100)

labelPump1 = tk.Label(text="BƠM VÀO",fg="#0000ff",font="Helvetica 15 bold")
labelPump1.place(x=750, y=370, width=100, height=50)

labelPump1 = tk.Label(text="BƠM RA",fg="#0000ff",font="Helvetica 15 bold")
labelPump1.place(x=860, y=370, width=100, height=50)

btn_pump_1 = ToggleButton(window)
btn_pump_1.setClickEvent(btn_pump_1_onClick)
btn_pump_1.button_place(750, 425)

btn_pump_2 = ToggleButton(window)
btn_pump_2.setClickEvent(btn_pump_2_onClick)
btn_pump_2.button_place(860, 425)

##### SUBCRIBE SERVER

def mqtt_callback(msg):
    print("Main.py  ---", msg)

    data = json.loads(msg)

    if data["station_id"] == "water_0001":
        for s in data["sensors"]:
            value = round(float(s["sensor_value"]), 2)
            print("Id", s["sensor_id"])
            print("Value", s["sensor_value"])
            if s["sensor_id"] == "ec_0001":
                labelWaterEC.config(text = value)
            if s["sensor_id"] == "ph_0001":
                labelWaterPH.config(text = value)
            if s["sensor_id"] == "ORP_0001":
                labelWaterORP.config(text = value)
            if s["sensor_id"] == "TEMP_0001":
                labelWaterTemp.config(text = value)

    if data["station_id"] == "soil_0001":
        for s in data["sensors"]:
            print("Name", s["sensor_name"])
            print("Value", s["sensor_value"])
            if s["sensor_id"] == "temp_0001":
                labelSoilTemp.config(text = s["sensor_value"])
            if s["sensor_id"] == "humi_0001":
                labelSoilHumi.config(text = s["sensor_value"])
            if s["sensor_id"] == "ph_0001":
                labelSoilPH.config(text = s["sensor_value"])
            if s["sensor_id"] == "EC_0001":
                labelSoilEC.config(text = s["sensor_value"])
            if s["sensor_id"] == "Nito_0001":
                labelSoilN.config(text =s["sensor_value"])
            if s["sensor_id"] == "Photpho_0001":
                 labelSoilP.config(text =s["sensor_value"])
            if s["sensor_id"] == "Kali_0001":
                labelSoilK.config(text =s["sensor_value"])

    if data["station_id"] == "air_0001":
        for s in data["sensors"]:
            print("Name", s["sensor_name"])
            print("Value", s["sensor_value"])
            if s["sensor_id"] == "temp_0001":
                labelAirTemp.config(text = s["sensor_value"])
            if s["sensor_id"] == "humi_0001":
                labelAirHumi.config(text = s["sensor_value"])
            if s["sensor_id"] == "illuminance_0001":
                labelAirLux.config(text = s["sensor_value"])
            if s["sensor_id"] == "CO2_0001":
                labelAirCO2.config(text = s["sensor_value"])

    # if station_id == "VALVE_0001":
    #     for s in sensors:
    #         print("Name", s["sensor_name"])
    #         print("Value", s["sensor_value"])
    #         if s["sensor_id"] == "valve_0001":
    #             btn_valve_1.update_button_click(s["sensor_value"])
    #             value1 = btn_var_1.get()
    #             if value1 != btn_valve_1.is_on: 
    #                 btn_valve_1_onClick(btn_valve_1.is_on)
    #                 value1 = btn_valve_1.is_on
    #         if s["sensor_id"] == "valve_0002":
    #             btn_valve_2.update_button_click(s["sensor_value"])
    #             value2 = btn_var_2.get()
    #             if value2 != btn_valve_2.is_on:
    #                 btn_valve_2_onClick(btn_valve_2.is_on)
    #                 value2 = btn_valve_2.is_on
    #         if s["sensor_id"] == "valve_0003":
    #             btn_valve_3.update_button_click(s["sensor_value"])
    #             value3 = btn_var_3.get()
    #             if value3 != btn_valve_3.is_on:
    #                 btn_valve_3_onClick(btn_valve_3.is_on)
    #                 value3 = btn_valve_3.is_on
    
    # if station_id == "PUMP_0001":
    #     for s in sensors:
    #         print("Name", s["sensor_name"])
    #         print("Value", s["sensor_value"])
    #         if s["sensor_id"] == "pump_0001":
    #             btn_pump_flow_1.update_button_click(s["sensor_value"])
    #             value_1 = btn_var1.get()
    #             if value_1 != btn_pump_flow_1.is_on:
    #                 btn_pump_flow_1_onClick(btn_pump_flow_1.is_on)
    #                 value_1 = btn_pump_flow_1.is_on
    #         if s["sensor_id"] == "pump_0002":
    #             btn_pump_flow_2.update_button_click(s["sensor_value"])
    #             value_2 = btn_var2.get()
    #             if value_2 != btn_pump_flow_2.is_on:
    #                 btn_pump_flow_2_onClick(btn_pump_flow_2.is_on)
    #                 value_2 = btn_pump_flow_2.is_on
    #         if s["sensor_id"] == "pump_0003":
    #             btn_pump_flow_3.update_button_click(s["sensor_value"])
    #             value_3 = btn_var3.get()
    #             if value_3 != btn_pump_flow_3.is_on:
    #                 btn_pump_flow_3_onClick(btn_pump_flow_3.is_on)
    #                 value_3 = btn_pump_flow_3.is_on
    #         if s["sensor_id"] == "pump_0004":
    #             btn_pump_1.update_button_click(s["sensor_value"])
    #             value_4 = btn_var4.get()
    #             if value_4 != btn_pump_1.is_on:
    #                 btn_pump_1_onClick(btn_pump_1.is_on)
    #                 value_4 = btn_pump_1.is_on
    #         if s["sensor_id"] == "pump_0005":
    #             btn_pump_2.update_button_click(s["sensor_value"])
    #             value_5 = btn_var5.get()
    #             if  value_5 != btn_pump_2.is_on:
    #                 btn_pump_2_onClick(btn_pump_2.is_on)
    #                 value_5 = btn_pump_2.is_on

mqttObject = MQTTHelper()
mqttObject.setRecvCallBack(mqtt_callback)

window.mainloop()
# while True:
#     window.update()
#     time.sleep(0.1)