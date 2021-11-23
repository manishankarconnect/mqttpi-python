
import json
from flask import Flask, render_template, request
from flask_mqtt import Mqtt
import datetime

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = "192.168.1.18"
app.config['MQTT_KEEPALIVE'] = 5

mqtt = Mqtt()
mqtt.init_app(app)

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
    
    msgs= [{"topic": "channel/Temp", "payload": {"data": "Temperature is {}".format(temp), "datetime": datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")}},
    {"topic": "channel/Vol", "payload": {"data": "Volume is {}".format(vol),"datetime": datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")}},
    {"topic": "channel/Visc", "payload": {"data": "Viscosity is {}".format(visc), "datetime": datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")}} ]
    
    for msg in msgs:
        mqtt.publish(msg["topic"], json.dumps(msg["payload"]))
    
    return render_template('index.html', pTemp=temp, pVol=vol, pVisc=visc)

   
if __name__ == '__main__':
    app.run(debug=True)