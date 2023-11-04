import paho.mqtt.client as mqtt

class MQTTHelper:

    MQTT_SERVER = "mqttserver.tk"
    MQTT_PORT = 1883
    MQTT_USERNAME = "innovation"
    MQTT_PASSWORD = "Innovation_RgPQAZoA5N"
    MQTT_TOPIC_PUB = "/innovation/soilmonitoring"
    MQTT_TOPIC_SUB_SOIL = "/innovation/soilmonitoring/"
    MQTT_TOPIC_SUB_WATER = "/innovation/watermonitoring/"
    MQTT_TOPIC_SUB_AIR = "/innovation/airmonitoring/"
    MQTT_TOPIC_SUB_VALVE = "/innovation/valvecontroller/"
    MQTT_TOPIC_SUB_PUMP = "/innovation/pumpcontroller/"
    recvCallBack = None

    def mqtt_connected(self, client, userdata, flags, rc):
        print("Connected succesfully!!")
        client.subscribe(self.MQTT_TOPIC_SUB_SOIL)
        client.subscribe(self.MQTT_TOPIC_SUB_WATER)
        client.subscribe(self.MQTT_TOPIC_SUB_AIR)
        #client.subscribe(self.MQTT_TOPIC_SUB_VALVE)
        #client.subscribe(self.MQTT_TOPIC_SUB_PUMP)

        
    def mqtt_subscribed(self, client, userdata, mid, granted_qos):
        print("Subscribed to Topic!!!")


    def mqtt_recv_message(self, client, userdata, message):
        #print("Received: ", message.payload.decode("utf-8"))
        self.recvCallBack(message.payload.decode("utf-8"))

    def __init__(self):

        self.mqttClient = mqtt.Client()
        self.mqttClient.username_pw_set(self.MQTT_USERNAME, self.MQTT_PASSWORD)
        self.mqttClient.connect(self.MQTT_SERVER, int(self.MQTT_PORT), 60)

        # Register mqtt events
        self.mqttClient.on_connect = self.mqtt_connected
        self.mqttClient.on_subscribe = self.mqtt_subscribed
        self.mqttClient.on_message = self.mqtt_recv_message

        self.mqttClient.loop_start()

    def setRecvCallBack(self, func):
        self.recvCallBack = func

    def publish(self, topic, message):
        self.mqttClient.publish(topic, str(message), retain=True)