# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program

def moveServo(degree):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	servoPin = 12
	GPIO.setup(servoPin,GPIO.OUT)  # Sets up pin 11 to an output (instead of an inp$
	p = GPIO.PWM(servoPin, 50)     # Sets up pin 11 as a PWM pin
	p.start(0)
	p.ChangeDutyCycle(degree)
	sleep(1)
	p.stop()
