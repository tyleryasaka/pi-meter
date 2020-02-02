from servo import moveServo
from clock import isFastingTime

if isFastingTime():
	moveServo(4)
else:
	moveServo(9)
