from os import system
import subprocess

class Terminal:
	@staticmethod
	def runCommand(_command):
		try:
			return [op_line.strip() for op_line in subprocess.check_output(_command).decode('utf-8').strip().split('\n')]
		except Exception as e:
			print("Subprocess Error, running as a command...\n")
			return system(_command)
		

if __name__ == "__main__":
	Terminal.runCommand("echo 'Working'")