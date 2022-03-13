Write-Output "Auto Power Mode Starting"
runas /user:Administrator .\nssm.exe start "AUTO_POWER_MODE"