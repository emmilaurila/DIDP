from temperature_converter import TemperatureConverter

def main():
    print("Program starting.")
    print("Initializing temperature converter...")
    converter = TemperatureConverter()
    print("Temperature converter initialized.")
    while True:
        print("\nOptions:")
        print("1) Set temperature")
        print("2) Convert to Celsius")
        print("3) Convert to Fahrenheit")
        print("4) Convert to Kelvin")
        print("0) Exit program")
        choice = input("Choice: ")
        if choice == "1":
            temp = float(input("Enter temperature: "))
            converter.setTemperature(temp)
            print(f"Temperature set to {temp}")
        elif choice == "2":
            print(f"Temperature in Celsius: {converter.toCelsius()}")
        elif choice == "3":
            print(f"Temperature in Fahrenheit: {converter.toFahrenheit()}")
        elif choice == "4":
            print(f"Temperature in Kelvin: {converter.toKelvin()}")
        elif choice == "0":
            print("Program ending.")
            break

if __name__ == "__main__":
    main()
