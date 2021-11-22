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
    if  request.method == 'POST':
        if not request.form.get("reset"):        
            temp = request.form.get("Temp")
            vol = request.form.get("Vol")
            visc = request.form.get("Visc")        
        else:
            temp = vol = visc = 50
        print(request.form)
        
    else:
        print(request.args)
    return render_template('index.html', pTemp=temp, pVol=vol, pVisc=visc)

   
if __name__ == '__main__':
    app.run(debug=True)