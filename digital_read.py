import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_23",GPIO.IN)

while 1:
	print(GPIO.input("P9_23"))

#while 1:
#	if GPIO.input("P9_23"):
#		GPIO.input("P9_23")

