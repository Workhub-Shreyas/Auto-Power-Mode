# **Auto Power Mode**

## **About**

* Built in Python
* Requires Powershell 15
* Requires Admin Access
* Automatically set Power Profile (Based on current status of Battery)
* Uses NSSM for managing of Service ( Non-Sucking Serivce Manager )

## **Features**

### 1. Easy Install
```ps1
    > .\install.bat
```

### 2. Easy Manage
```ps1
    > .\nssm.exe start "AUTO_POWER_MODE"
    > .\nssm.exe status "AUTO_POWER_MODE"
    > .\nssm.exe stop "AUTO_POWER_MODE"
```

### 3. Easy Uninstall
```ps1
    > .\uninstall.bat
```