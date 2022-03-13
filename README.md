# ![Logo](autopowermode.ico) **Auto Power Mode**

## **About**

* Built in Python
* Requires Powershell 15
* Requires Admin Access
* Automatically set Power Profile (Based on current status of Battery)
* Uses NSSM for managing of Service ( Non-Sucking Serivce Manager )

## **Features**

#### 1. Detect Battery status
```python
    >>> from batterystats import Battery
    >>> Battery.get("EstimatedChargeRemaining")
    83
    >>> Battery.isCharging()
    True
    >>> Battery.isLowCharge()
    False
```

#### 2. Identify Available Power Profiles
```python
    >>> from powermode import POWER_MODE
    >>> from powermode import POWER_MODE
    >>> POWER_MODE.ACTIVE
    'Performance'
    >>> POWER_MODE.AVAILABLE_MODES
    {'Performance': '1439c6a1-dc3f-49a1-9e1d-a3ec250f1b27', 'Balanced': '381b4222-f694-41f0-9685-ff5bb260df2e', 'Battery': '954c251e-b74f-496d-bc44-5ed7358c8676'}
```

#### 3. Actual Script Runs as a Service
```ps1
    > python .\autopowermode.py
    1647137080.2369092 : 
    Battery is Charging
    Changing profile to Performance => Performance is already active.
    ------------------------------
```

## **Steps for Service Management**
<small>( Only Use POWERSHELL 15 for this )</small>

#### 1. To Install
```ps1
    > .\nssm.exe install "AUTO_POWER_MODE" "<Full_Python_Exec_Path>" "$(pwd)\autopowermode.py"
    > .\nssm.exe set "AUTO_POWER_MODE" AppStderr "$(pwd)\logs\power.log"
    > .\nssm.exe set "AUTO_POWER_MODE" AppStderr "$(pwd)\logs\errors\power-errors.log"
    > .\nssm.exe start "AUTO_POWER_MODE"
```

#### 2. To Manage
```ps1
    > .\nssm.exe start "AUTO_POWER_MODE"
    > .\nssm.exe status "AUTO_POWER_MODE"
    > .\nssm.exe stop "AUTO_POWER_MODE"
```

#### 3. To Uninstall
```ps1
    > .\nssm.exe stop "AUTO_POWER_MODE"
    > .\nssm.exe remove "AUTO_POWER_MODE" confirm
```