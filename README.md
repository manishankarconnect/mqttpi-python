# MQTTpi-Python
*Communicate between Windows PC to Raspberry pi with pi as broker itself.*

Use ***Raspberry Pi 4 Model B*** for setting up.

![](https://raspberry-valley.azurewebsites.net/img/MQTT-on-Raspberry-Pi-01.png)

### MQTT Broker in Pi:

#### Install Python MQTT Library On raspberry Pi:
    sudo apt-get install -y mosquitto mosquitto-clients

#### Run Broker:
    sudo systemctl enable mosquitto

#### Verify Broker Active:
    sudo systemctl status mosquitto
Check "Active: active (running)" in the output.


### MQTT Publisher (Windows PC):
#### Install paho-mqtt in PC:
Install Python3 on Windows and install `paho-mqtt` using the command
### 
    pip3 install paho-mqtt


### MQTT Subscriber (Raspberry Pi):

#### Install paho-mqtt in pi:
    sudo pip3 install paho-mqtt


### How to Run the MQTT:

1. Open "mqttpc.py" and provide the pi ip-address as "MQTT_SERVER"
2. Run the "mqttpc.py" in Windows using python, which acts a publisher.
3. Now the messages are sent to the broker (which is pi).
4. Now run the "mqttpi.py" in pi, which act as a subscriber and check the messages sent by windows is received by the pi.

#### Note: 
1. ***Single message pub/sub:***
   1. Tag: `Paho-MQTT-Single`

2. ***Multi message pub/sub:***
   1. Tag: `Paho-MQTT-Multiple`
   2. Added JSON for transmitting & receiving different data in payload.

3. ***Flask MQTT:***
   1. Run *flask/app.py*
   2. Tag: `Flask-MQTT-Release`
   3. Implemented Flask-MQTT to publish message.
    ![](demos\Flask-MQTT-Shot.jpg)


Refer below recordings for demo:
1. `"MQTT Windows to Pi communication Python.mp4"` - Paho-MQTT.
2. `Flask-MQTT-Demo.mp4` - Flask-MQTT
