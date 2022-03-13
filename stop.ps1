Write-Output "Auto Power Mode Stopping"
runas /user:Administrator .\nssm.exe stop "AUTO_POWER_MODE"