import paho.mqtt.publish as publish
import datetime
import keyboard
import time
import random
import json
 
MQTT_SERVER = "192.168.1.18"
MQTT_PATH = "channel"
SUBPATH = ["Temp", "Vol", "Visc"]


def append_datetime(msgs):
    now = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")    
    for topic in msgs:
        
        if type(topic["payload"]) is str:
            topic["payload"] = json.loads(topic["payload"])        
        topic["payload"]["datetime"] = now
        topic["payload"] = json.dumps(topic["payload"])                
    return msgs

while True:
    msgs= [{"topic": "channel/Temp", "payload": {"data": "Temperature is {}".format(random.randrange(0, 100)), "datetime": None}},
        {"topic": "channel/Vol", "payload": {"data": "Volume is {}".format(random.randrange(0, 100)),"datetime": None}},
        {"topic": "channel/Visc", "payload": {"data": "Viscosity is {}".format(random.randrange(0, 100)), "datetime": None}} ]
    
    append_datetime(msgs)        
    publish.multiple(msgs, hostname=MQTT_SERVER, keepalive=60)
    time.sleep(0.5)
    if keyboard.is_pressed("q"):
        exit(0)
