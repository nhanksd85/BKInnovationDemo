import json
class PumpStation:
    station_id = "PUMP_0001"
    station_name = "Hệ Thống Bơm"
    gps_longitude = 106.89
    gps_latitude = 10.5
    sensors = []

    def __init__(self, _id, _name, _long, _lat):
        self.station_id = _id
        self.station_name = _name
        self.gps_longitude = _long
        self.gps_latitude = _lat
        self.sensors = []
        pass

    def addPump(self, aPump):
        self.sensors.append(aPump)

    def to_json(self):
        return {
            "station_id": self.station_id,
            "station_name": self.station_name,
            "gps_longitude": self.gps_longitude,
            "gps_latitude": self.gps_latitude,
            "sensors": [x.to_json() for x in self.sensors]
            }