from time import sleep, time
from batterystats import Battery
from powermode import POWER_MODE

try:
	for i in range(100):
		print(f"{time()} : ")
		# print("isCharging   : ", Battery.isCharging())
		# print("isBatteryLow : ", Battery.isLowCharge())
		if Battery.isCharging():
			print("Battery is Charging")
			POWER_MODE.SET('Performance')
		else:
			if not Battery.isLowCharge():
				print("Battery is Medium")
				POWER_MODE.SET('Balanced')
			else:
				print("Battery is Low")
				POWER_MODE.SET('Battry')
		print("---"*10)
		sleep(60)
except KeyboardInterrupt as k:
	print("Forcefully Exiting")