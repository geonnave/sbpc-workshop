import time
from gpio import GPIO

led_pin = GPIO(0, "out")

while True:
	print("Ligando LED")
	led_pin.write(GPIO.HIGH)
	time.sleep(1)

	print("Desligando LED")
	led_pin.write(GPIO.LOW)
	time.sleep(1)