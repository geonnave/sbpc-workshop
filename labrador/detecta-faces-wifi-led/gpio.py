import os

class GPIO():
	LOW = 0
	HIGH = 1

	def __init__(self, pin, mode):
		self.pin = pin
		self.mode = mode
		os.system("gpio mode %d %s" % (pin, mode))
	
	def write(self, value):
		os.system("gpio write %d %d" % (self.pin, value))
