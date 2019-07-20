import time
from gpio import GPIO

led_pin = GPIO(0, "out")

while True:
	led_pin.write(1)
	time.sleep(1)
	led_pin.write(0)
	time.sleep(1)