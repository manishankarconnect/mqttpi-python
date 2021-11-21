import paho.mqtt.client as mqtt #import library
import json
 
MQTT_SERVER = "localhost" #specify the broker address, it can be IP of raspberry pi or simply localhost
MQTT_PATH = "channel/Temp" #this is the name of topic, like temp

req_list = ["channel/Temp", "channel/Vol"]
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for topic in req_list:
        client.subscribe(topic)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    print(msg.topic +" "+ str(payload["datetime"]) + " " + str(payload["data"]))    
    # more callbacks, etc
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER)
client.loop_forever()# use this line if you don't want to write any further code. It blocks the code forever to check for data
#client.loop_start()  #use this line if you want to write any more code here