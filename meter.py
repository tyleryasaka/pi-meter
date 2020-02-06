from servo import moveServo

def setMeter(val):
	if val == 1:
		moveServo(8)
	elif val == 2:
		moveServo(6.5)
	elif val == 3:
		moveServo(5)

