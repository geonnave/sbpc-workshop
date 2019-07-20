from gpio import GPIO
from flask import Flask, render_template, Response
import json

app = Flask(__name__)
led_pin = GPIO(0, "out")
led_status = 0

@app.route('/led')
def led():
    global led_status
    if led_status == 0:
        print("Ligando LED")
        led_status = 1
        led_pin.write(led_status)
    else:
        print("Desligando LED")
        led_status = 0
        led_pin.write(led_status)
    return json.dumps({"led_status": led_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040, debug=True)