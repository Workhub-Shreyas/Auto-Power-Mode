from random import random
from time import sleep
from pip import main
from Terminal import Terminal

class _POWER_MODE:
	class AlreadyActiveException(Exception):
		pass

	@property
	def AVAILABLE_MODES(self):
		LIST_AVAILABLE = {}
		pwr_conf = [row.split() for row in Terminal.runCommand("powercfg /L")[2:]]
		for row in pwr_conf:
			mode_guid, mode_name = row[3], row[4].lstrip('(').rstrip(')')
			LIST_AVAILABLE[mode_name] = mode_guid
		return LIST_AVAILABLE

	@property
	def ACTIVE(self):
		return self.GET()
	
	def GET(self):
		return Terminal.runCommand("powercfg /GETACTIVESCHEME")[0].split()[4].lstrip('(').rstrip(')')

	def SET(self, mode):
		try :
			print (f"Changing profile to {mode}", end=" => ")
			if mode == self.ACTIVE:
				raise _POWER_MODE.AlreadyActiveException(mode )
			Terminal.runCommand(f"powercfg /S {self.AVAILABLE_MODES[mode]}")
			print("Success")

		except _POWER_MODE.AlreadyActiveException:
			print(f"{mode} is already active.")

		except Exception as e:
			print("Power Profile Not Found : ",e)
			print("\nAvaiable Modes : \n"+('-----'*10))
			for profie_name in self.AVAILABLE_MODES:
				print(f"{profie_name} \t:\t{self.AVAILABLE_MODES[profie_name]}")
			print()
			return 1
	
POWER_MODE = _POWER_MODE()

if __name__ == "__main__":
	active_mode = POWER_MODE.ACTIVE
	print(f"Current Mode : {active_mode}\n")

	try :
		print("Testing Setting of all Modes\n"+('-----'*10))
		for i, mode in enumerate(POWER_MODE.AVAILABLE_MODES):
			print(i+1, end=" : ")
			POWER_MODE.SET(mode)
			sleep(2)
		print(('-----'*10)+"\nAll Modes Tested Successfully\n"+('-----'*10))
	except Exception as e:
		print(e)
	except KeyboardInterrupt:
		print("\nCANCEL REQUESTED\n")
		pass

	print(f"\nResetting Mode to previous active : {active_mode}")
	POWER_MODE.SET(active_mode)

	print("\nDone.")