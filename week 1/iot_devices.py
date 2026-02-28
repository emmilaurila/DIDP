class IoTDevice:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location
        self.data = None
    def update_data(self, value):
        raise NotImplementedError("Subclasses must implement update_data")
    def to_csv_row(self):
        return [self.__class__.__name__, self.device_id, self.location, self.data]


class TemperatureSensor(IoTDevice):
    def update_data(self, value=None):
        while True:
            try:
                if value is None:
                    value = input("Enter temperature value: ")
                val = float(value)
                self.data = val
                break
            except ValueError:
                print("Enter numeric value.")
                value = None


class HumiditySensor(IoTDevice):
    def update_data(self, value=None):
        while True:
            try:
                if value is None:
                    value = float(input("Enter humidity value (0-100): "))
                else:
                    value = float(value)
                if 0 <= value <= 100:
                    self.data = value 
                    break
                else:
                    print("Humidity must be between 0 and 100")
                    value = None
            except ValueError:
                print("Enter numeric value.")
                value = None
                
class MotionSensor(IoTDevice):
    def update_data(self, value=None):
        while True:
            try:
                if value is None:
                    value = input("Enter motion value (True/False): ")
                if isinstance(value, str):
                    if value.lower() == "true":
                        self.data = True
                        break
                    elif value.lower() == "false":
                        self.data = False
                        break
                    else:
                        print("Motion must be True or False.")
                        value = None
                elif isinstance(value, bool):
                    self.data = value
                    break
                else:
                    print("Motion must be True or False.")
                    value = None
            except Exception:
                print("Invalid input.")
                value = None
