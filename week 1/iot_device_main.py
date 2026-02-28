import csv
from iot_devices import IoTDevice, TemperatureSensor, HumiditySensor, MotionSensor

filename = "iot_data.csv"
devices = []

def add_device():
        device_id = input("\nEnter device ID: ")
        location = input("Enter device location: ")
        print("Select sensor type:")
        print("1 - Temperature")
        print("2 - Humidity")
        print("3 - Motion")

        sensor_choice = input("Choice: ")
        if sensor_choice == "1":
            device = TemperatureSensor(device_id, location)
            value = float(input("Enter temperature value: "))
            device.update_data(value)
        elif sensor_choice == "2":
            device = HumiditySensor(device_id, location)
            value = float(input("Enter humidity value (0-100): "))
            device.update_data(value)
        elif sensor_choice == "3":
            device = MotionSensor(device_id, location)
            value = input("Enter motion value (True or False): ")
            device.update_data(value)
        else:
            print("Invalid sensor.")
            return
        devices.append(device)
        print("IoT device added")

def serialize_data():
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["type", "device_id", "location", "data"])
            for d in devices:
                writer.writerow(d.to_csv_row())
        print("\nData serialized to", filename)

def deserialize_data():
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)

            devices.clear()

            for row in reader:
                sensor_type, device_id, location, data = row

                if sensor_type == "TemperatureSensor":
                    device = TemperatureSensor(device_id, location)
                    device.update_data(float(data))
                elif sensor_type == "HumiditySensor":
                    device = HumiditySensor(device_id, location)
                    device.update_data(float(data))
                elif sensor_type == "MotionSensor":
                    device = MotionSensor(device_id, location)
                    device.update_data(data)
                else:
                    continue
                devices.append(device)
        print("\nData deserialized from", filename)
    except FileNotFoundError:
        print("File not found:", filename)

def main():
    print("Program starting.")

    while True:
        print("\n1 - Add IoT Device")
        print("2 - Serialize Data")
        print("3 - Deserialize Data")
        print("0 - Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_device()
        elif choice == "2":
            serialize_data()
        elif choice == "3":
            deserialize_data()
        elif choice == "0":
            print("\nExiting program.")
            break
        else:
            print("\nInvalid menu choice. Select a number.")

if __name__ == "__main__":
    main()
