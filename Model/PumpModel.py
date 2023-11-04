class Pump():
    sensor_id =  "pump_0001"
    sensor_name = "Phân khu 1"
    sensor_value = 1
    sensor_unit = ""

    def __init__(self, _id, _name, _value, _unit):
        self.sensor_id = _id
        self.sensor_name = _name
        self.sensor_value = _value
        self.sensor_unit = _unit
    def to_json(self):
        return {
            "sensor_id": self.sensor_id,
            "sensor_name" : self.sensor_id,
            "sensor_value" : self.sensor_value,
            "sensor_unit" : self.sensor_unit
        }
