from simulation import Player, NPC, Object, interact_all_entities

def main():
    entities = []
    while True:
        print("Virtual Reality Simulation\n")
        print("1 - Add Entity")
        print("2 - Interact with Entities")
        print("3 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("\nEnter entity name: ")
            position = input("Enter location: ")
            print("\nSelect Entity Type:")
            print("1 - Player")
            print("2 - NPC")
            print("3 - Object")
            entity_type = input("Choice: ")

            if entity_type == "1":
                try:
                    level = int(input("\nEnter player level: "))
                    entities.append(Player(name, position, level))
                    print("\nPlayer added successfully.\n")
                except ValueError:
                    print("Level must be a number.\n")

            elif entity_type == "2":
                role = input("\nEnter NPC role: ")
                entities.append(NPC(name, position, role))
                print("NPC added successfully.\n")

            elif entity_type == "3":
                object_type = input("\nEnter object type: ")
                entities.append(Object(name, position, object_type))
                print("Object added successfully.\n")
            else:
                print("Invalid entity type.")

        elif choice == "2":
            if not entities:
                print("No entities to interact with.")
            else:
                interact_all_entities(entities)

        elif choice == "3":
            print("Exiting simulation.")
            break
        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    main()