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

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
# try:
#     ser = serial.Serial(port="COM7", baudrate=115200)
# except:
#     print("Modbus485**","Failed to write data")


m485 = Utilities.modbus485.Modbus485(ser)

window = tk.Tk()

# is_on = False
# def toggle_button_click_1():
#     global  is_on
#     print("Button 1 is clicked")
#     if is_on:
#         on_button_v1.config(image=off)
#         is_on = False
#         #m485.modbus485_send(relay1_OFF)
#     else:
#         on_button_v1.config(image=on)
#         is_on = True
#         #m485.modbus485_send(relay1_ON)

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


window.attributes('-fullscreen', True)
#window.geometry("1024x600")
window.title("Rapido Project")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)

##### SOIL LABEL

labelSoil = tk.Label(text="ĐẤT TRỒNG",fg="#ff0000",justify=CENTER,font="Helvetica 20 bold")
labelSoil.place(x=50, y=0, width=300, height=100)

labelSoil = tk.Label(text="NHIỆT ĐỘ (°C)",fg="#ff0000",justify=CENTER,font="Helvetica 15")
labelSoil.place(x=50, y=80, width=150, height=20)
labelSoil = tk.Label(text="ĐỘ ẨM (%)",fg="#ff0000",justify=CENTER,font="Helvetica 15")
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

labelAir = tk.Label(text="KHÔNG KHÍ",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAir.place(x=350, y=0, width=300, height=100)

labelAir = tk.Label(text="NHIỆT ĐỘ (°C)",fg="#099940",justify=CENTER,font="Helvetica 15")
labelAir.place(x=350, y=80, width=150, height=20)
labelAir = tk.Label(text="ĐỘ ẨM (%)",fg="#099940",justify=CENTER,font="Helvetica 15")
labelAir.place(x=500, y=80, width=150, height=20)

labelAirTemp = tk.Label(text="335",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAirTemp.place(x=350, y = 100, width=150)

labelAirHumi = tk.Label(text="700",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAirHumi.place(x=500, y = 100, width=150)

labelAir = tk.Label(text="Độ sáng",fg="#099940",justify=CENTER,font="Helvetica 15")
labelAir.place(x=350, y=150, width=150, height=20)
labelAir = tk.Label(text="CO2",fg="#099940",justify=CENTER,font="Helvetica 15")
labelAir.place(x=500, y=150, width=150, height=20)

labelAirCO2 = tk.Label(text="5",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAirCO2.place(x=350, y = 170, width=150)

labelAirLux = tk.Label(text="10",fg="#099940",justify=CENTER,font="Helvetica 20 bold")
labelAirLux.place(x=500, y = 170, width=150)

##### WATER LABEL

labelWater = tk.Label(text="NƯỚC TƯỚI",fg="#0000ff",justify=CENTER,font="Helvetica 20 bold")
labelWater.place(x=700, y=0, width=300, height=100)

labelWater = tk.Label(text="NHIỆT ĐỘ (°C)",fg="#0000ff",justify=CENTER,font="Helvetica 15")
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
    station_id = data["station_id"]
    sensors = data["sensors"]
    if station_id == "water_0001":
        for s in sensors:
            print("Name", s["sensor_name"])
            print("Value", s["sensor_value"])
            if s["sensor_id"] == "ec_0001":
                labelWaterEC.config(text = s["sensor_value"])
            if s["sensor_id"] == "ph_0001":
                labelWaterPH.config(text = s["sensor_value"])
            if s["sensor_id"] == "ORP_0001":
                labelWaterORP.config(text = s["sensor_value"])
            if s["sensor_id"] == "TEMP_0001":
                labelWaterTemp.config(text = s["sensor_value"])

    if station_id == "soil_0001":
        for s in sensors:
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

    if station_id == "air_0001":
        for s in sensors:
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

    if station_id == "VALVE_0001":
        for s in sensors:
            print("Name", s["sensor_name"])
            print("Value", s["sensor_value"])
            if s["sensor_id"] == "valve_0001":
                btn_valve_1.update_button_click(s["sensor_value"])
                btn_valve_1_onClick(btn_valve_1.is_on)
            if s["sensor_id"] == "valve_0002":
                btn_valve_2.update_button_click(s["sensor_value"])
                btn_valve_2_onClick(btn_valve_2.is_on)
            if s["sensor_id"] == "valve_0003":
                btn_valve_3.update_button_click(s["sensor_value"])
                btn_valve_3_onClick(btn_valve_3.is_on)
    
    if station_id == "PUMP_0001":
        for s in sensors:
            print("Name", s["sensor_name"])
            print("Value", s["sensor_value"])
            if s["sensor_id"] == "pump_0001":
                btn_pump_flow_1.update_button_click(s["sensor_value"])
                btn_pump_flow_1_onClick(btn_pump_flow_1.is_on)
            if s["sensor_id"] == "pump_0002":
                btn_pump_flow_2.update_button_click(s["sensor_value"])
                btn_pump_flow_2_onClick(btn_pump_flow_2.is_on)
            if s["sensor_id"] == "pump_0003":
                btn_pump_flow_3.update_button_click(s["sensor_value"])
                btn_pump_flow_3_onClick(btn_pump_flow_3.is_on)
            if s["sensor_id"] == "pump_0004":
                btn_pump_1.update_button_click(s["sensor_value"])
                btn_pump_1_onClick(btn_pump_1.is_on)
            if s["sensor_id"] == "pump_0005":
                btn_pump_2.update_button_click(s["sensor_value"])
                btn_pump_2_onClick(btn_pump_2.is_on)

mqttObject = MQTTHelper()
mqttObject.setRecvCallBack(mqtt_callback)

window.mainloop()

# while True:
#     window.update()
#     time.sleep(0.1)