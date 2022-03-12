import subprocess, sys
from Terminal import Terminal

class Battery:
	ALLOWED_PARAMETERS = [
		'Availability',
		'BatteryRechargeTime',
		'BatteryStatus',
		'Caption',
		'Chemistry',
		'ConfigManagerErrorCode',
		'ConfigManagerUserConfig',
		'CreationClassName',
		'Description',
		'DesignCapacity',
		'DesignVoltage',
		'DeviceID',
		'ErrorCleared',
		'ErrorDescription',
		'EstimatedChargeRemaining',
		'EstimatedRunTime',
		'ExpectedBatteryLife',
		'ExpectedLife',
		'FullChargeCapacity',
		'InstallDate',
		'LastErrorCode',
		'MaxRechargeTime',
		'Name',
		'PNPDeviceID',
		'PowerManagementCapabilities',
		'PowerManagementSupported',
		'SmartBatteryVersion',
		'Status',
		'StatusInfo',
		'SystemCreationClassName',
		'SystemName',
		'TimeOnBattery',
		'TimeToFullCharge'
	]

	@staticmethod
	def get (_parameter):
		output_value = 0
		try :
			if not _parameter in Battery.ALLOWED_PARAMETERS:
				raise Exception(f"Invalid Parameter '{_parameter}'")
			output = Terminal.runCommand(f"WMIC PATH Win32_Battery Get {_parameter}")
			if len(output)==1:
				output = ''
			else:
				output = output[1]
		except Exception as e:
			print(f"Error : {e}")
			output = "ERR"
		finally:
			output_value =  int(output) if output.isnumeric() else output
		return output_value
	
	@staticmethod
	def currentCharge():
		return Battery.get("EstimatedChargeRemaining")

	@staticmethod
	def isCharging():
		return Battery.get("BatteryStatus") == 2

	@staticmethod
	def isLowCharge():
		return Battery.currentCharge() <= 50

if __name__ == '__main__':
	if(len(sys.argv) != 1):
		for param in sys.argv[1:]:
			print(f"{param} : {Battery.get(param)}")
	else:
		for param in Battery.ALLOWED_PARAMETERS:
			print(f"{param} : {Battery.get(param)}")