import eventlet
import json
from flask import Flask, render_template, request
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

eventlet.monkey_patch()
app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = "192.168.1.18"
app.config['MQTT_KEEPALIVE'] = 5

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/", methods= ['POST', 'GET'])
def read():
    temp = request.form["Tempval"]
    vol = request.form["Volval"]
    visc = request.form["Viscval"]
    print("Viscosity" + visc)
    output = visc
    return render_template('index.html',output=output)

   
if __name__ == '__main__':
    app.run(debug=True)