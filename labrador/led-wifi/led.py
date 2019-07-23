from gpio import GPIO
from flask import Flask, render_template, Response
import json

app = Flask(__name__)
led_pin = GPIO(0, "out")
led_status = GPIO.LOW

@app.route('/')
def index():
    return json.dumps({"info": "acesse a rota /led"})

@app.route('/led')
def led():
    global led_status
    if led_status == GPIO.LOW:
        print("Ligando LED")
        # COMPLETAR
    else:
        print("Desligando LED")
        # COMPLETAR
    return json.dumps({"led_status": led_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040, debug=True)