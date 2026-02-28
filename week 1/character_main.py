from character import GameCharacter, Warrior, Mage, Archer, simulate_battle

def main():
    characters = []
    while True:
        print("Program starting.\n")
        print("1 - Create Character")
        print("2 - Simulate Battle")
        print("0 - Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter character name: ")
            print("Select character type:")
            print("1 - Warrior")
            print("2 - Mage")
            print("3 - Archer")
            type_choice = input("Choice: ")
            if type_choice == "1":
                characters.append(Warrior(name))
                print(f"Warrior {name} created.")
            elif type_choice == "2":
                characters.append(Mage(name))
                print(f"Mage {name} created.")
            elif type_choice == "3":
                characters.append(Archer(name))
                print(f"Archer {name} created.")
            else:
                print("Invalid character type.")
        elif choice == "2":
            if not characters:
                print("No characters.")
            else:
                simulate_battle(characters)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    main()