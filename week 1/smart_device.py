class SmartDevice:
    def __init__(self, device_name, status=False):
        self.device_name = device_name
        self.status = status

class SmartLight(SmartDevice):
    def __init__(self, device_name, status=False, brightness=50):
        super().__init__(device_name, status)
        self.brightness = brightness 

    def operate(self):
        self.status = not self.status
        action = "ON" if self.status else "OFF"
        print(f"{self.device_name} light turned {action} at brightness {self.brightness}%")

class SmartThermostat(SmartDevice):
    def __init__(self, device_name, temperature, status=False):
        super().__init__(device_name, status)
        self.temperature = temperature

    def operate(self):
        self.status = not self.status
        action = "active" if self.status else "inactive"
        print(f"{self.device_name} thermostat is {action}, set to {self.temperature}°C")

class SmartLock(SmartDevice):
    def __init__(self, device_name, status=False):
        super().__init__(device_name, status)

    def operate(self):
        self.status = not self.status
        action = "locked" if self.status else "unlocked"
        print(f"{self.device_name} is now {action}")

def operate_all_devices(devices):
    print("\nStarting operation\n")
    for device in devices:
        device.operate()
    print("\nOperation done\n")