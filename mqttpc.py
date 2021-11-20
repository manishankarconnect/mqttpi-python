import paho.mqtt.publish as publish
 
MQTT_SERVER = "192.168.1.18"
MQTT_PATH = "channel"
SUBPATH = ["Temp", "Vol", "Visc"]
import time
while True:
    publish.single(MQTT_PATH + "/" + SUBPATH[0], "Temperature is 25", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    publish.single(MQTT_PATH + "/" + SUBPATH[1], "Volume is 84", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    publish.single(MQTT_PATH + "/" + SUBPATH[2], "Visc is 25", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    time.sleep(3)