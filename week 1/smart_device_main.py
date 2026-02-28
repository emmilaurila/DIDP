from smart_device import SmartDevice, SmartLight, SmartThermostat, SmartLock, operate_all_devices

def main():
    devices = []
    while True:
        print("Program starting.\n")
        print("1 - Add Smart Device")
        print("2 - Operate Devices")
        print("0 - Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter device name: ")
            print("\nSelect device type: ")
            print("1 - Smart Light")
            print("2 - Smart Thermostat")
            print("3 - Smart Lock")
            device_choice = input("\nChoice: ")

            if device_choice == "1":
                 while True:
                    try:
                           brightness = int(input("Enter brightness (0-100): "))
                           if 0 <= brightness <= 100:
                               devices.append(SmartLight(name, brightness=brightness))
                               print(f"\nDevice set to {brightness}\n")
                               break
                           else:
                               print("Brightness must be between 0 and 100.") 
                    except ValueError:
                         print("Please enter a numeric value.")

            elif device_choice == "2":
                try:
                    temp = float(input("Enter temperature (°C): "))
                    devices.append(SmartThermostat(name, temperature=temp))
                    print(f"\nSmart Thermostat '{name}' added and set to {temp}°C\n")
                except ValueError:
                    print("Invalid input.")

            elif device_choice == "3":
                devices.append(SmartLock(name))
                print(f"Smart Lock '{name}' added.\n")
            else:
                print("Invalid device type.")

        elif choice == "2":
            if not devices:
                print("No device to operate.")
            else:
                operate_all_devices(devices)

        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()