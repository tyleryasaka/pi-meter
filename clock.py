from datetime import datetime

def isFastingTime():
	now = datetime.now()
	isOddDay = (now.day % 2) == 1
	return (isOddDay and now.hour > 12) or ((not isOddDay) and (now.hour < 7))

