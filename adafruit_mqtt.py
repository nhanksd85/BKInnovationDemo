import sys
from Adafruit_IO import MQTTClient

class Adafruit_MQTT:
    AIO_FEED_IDs = ["button1", 	"button2"]
    AIO_USERNAME = "NPNLab_BBC"
    AIO_KEY = "aio_hwsd42NcU25IN3fMkwo4tJ3OHIO6"

    def connected(self, client):
        print("Ket noi thanh cong ...")
        for feed in self.AIO_FEED_IDs:
            client.subscribe(feed)

    def subscribe(self, client , userdata , mid , granted_qos):
        print("Subscribe thanh cong ...")

    def disconnected(self, client):
        print("Ngat ket noi ...")
        sys.exit (1)

    def message(self, client , feed_id , payload):
        print("Nhan du lieu: " + payload)

    def __init__(self):
        client = MQTTClient(self.AIO_USERNAME , self.AIO_KEY)
        client.on_connect = self.connected
        client.on_disconnect = self.disconnected
        client.on_message = self.message
        client.on_subscribe = self.subscribe
        client.connect()
        client.loop_background()

