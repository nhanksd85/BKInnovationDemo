import json
from Model.PumpStationModel import *
from Model.PumpModel import *

class SwitchModel:
    name = ""
    status = False

button1 = Pump("pump_0001", "Phân Khu 1", 0, "")
button2 = Pump("pump_0002", "Phân Khu 2", 0, "")





arraybutton = []
arraybutton.append(button1)
arraybutton.append(button2)

# convert into JSON:
#y = json.dumps(a.__dict__ for a in arraybutton)
y = json.dumps(arraybutton, default = lambda x: x.__dict__)
# the result is a JSON string:
print(y)

aStation = PumpStation()
aStation.addPump(button1)
aStation.addPump(button2)
print(aStation.to_json())


