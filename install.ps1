set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/c cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

.\nssm.exe install "AUTO_POWER_MODE" "C:\Users\$(($(whoami) -split '\\')[1])\AppData\Local\Programs\Python\Python310\python.exe" "$(pwd)\autopowermode.py"
.\nssm.exe set "AUTO_POWER_MODE" AppStderr "$(pwd)\logs\power.log"
.\nssm.exe set "AUTO_POWER_MODE" AppStderr "$(pwd)\logs\errors\power-errors.log"

.\start