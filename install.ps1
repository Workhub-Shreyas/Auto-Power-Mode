.\nssm.exe install "AUTO_POWER_MODE" "C:\Users\$(($(whoami) -split '\\')[1])\AppData\Local\Programs\Python\Python310\python.exe" "$(pwd)\autopowermode.py"
.\nssm.exe set "AUTO_POWER_MODE" AppStderr "$(pwd)\logs\power.log"
.\nssm.exe set "AUTO_POWER_MODE" AppStderr "$(pwd)\logs\errors\power-errors.log"

.\start