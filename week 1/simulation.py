class Entity:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def interact(self):
        raise NotImplementedError("Subclasses must implement interact()")

class Player(Entity):
    def __init__(self, name, position, level):
        super().__init__(name, position)
        self.level = level
    def interact(self):
        print(f"Player {self.name} (Level {self.level}) explores the {self.position}.")

class NPC(Entity):
    def __init__(self, name, position, role):
        super().__init__(name, position)
        self.role = role
    def interact(self):
        print(f"NPC {self.name} the {self.role} gives you a quest at {self.position}.")

class Object(Entity):
    def __init__(self, name, position, object_type):
        super().__init__(name, position)
        self.object_type = object_type
    def interact(self):
        print(f"Object {self.name} ({self.object_type}) can be examined at {self.position}.")

def interact_all_entities(entities):
    print("\n-Interaction with entities\n")
    for entity in entities:
        entity.interact()
    print("\nInteraction complete\n")