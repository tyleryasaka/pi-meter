# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
servoPin = 12
GPIO.setup(servoPin,GPIO.OUT)
p = GPIO.PWM(servoPin, 50)

def moveServo(degree):
	p.start(degree)
	sleep(1)
	p.stop()
	GPIO.cleanup()
