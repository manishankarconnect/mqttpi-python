# mqttpi-python
Communicate between Windows PC to Raspberry pi with pi as broker itself.

Use Raspberry Pi 4 Model B for setting up.


MQTT Broker in Pi:

Install Python MQTT Library On raspberry Pi:
    sudo apt-get install -y mosquitto mosquitto-clients

Run Broker:
    sudo systemctl enable mosquitto

Verify Broker Active:
    sudo systemctl status mosquitto
    Check "Active: active (running)" in the output.


MQTT Publisher (Windows PC):

Have Python3 on Windows and install paho-mqtt using the below command.
    pip3 install paho-mqtt


MQTT Subscriber (Raspberry Pi):

Install paho-mqtt in pi:
    sudo pip3 install paho-mqtt


How to Run the MQTT:

Now open "mqttpc.py" and provide the pi ip-address as "MQTT_SERVER"
Run the "mqttpc.py" in Windows using python, which acts a publisher.
Now the messages are sent to the broker (which is pi).

Now run the "mqttpi.py" in pi, which act as a subscriber and check the messages sent by windows is received by the pi.

