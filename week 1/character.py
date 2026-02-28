from abc import ABC, abstractmethod

class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def defend(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print(f"{self.name} attacks with a sword")
    def defend(self):
        print(f"{self.name} dodges the attack.")
class Mage(GameCharacter):
    def attack(self):
        print(f"{self.name} attacks with a spell.")
    def defend(self):
        print(f"{self.name} dodges the attack.")
class Archer(GameCharacter):
    def attack(self):
        print(f"{self.name} attacks with a bow and arrow.")
    def defend(self):
        print(f"{self.name} dodges the attack.")

def simulate_battle(characters):
    print("\nSimulated battle starts\n")
    for character in characters:
        character.attack()
        character.defend()
    print("\nSimulated battle ends\n")

