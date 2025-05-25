class Player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.inventory = []
        self.location = "forest"

    def add_item(self, item):
        """Add item to inventory"""
        if item not in self.inventory:
            self.inventory.append(item)
            return True
        return False

    def has_item(self, item):
        """Check if player has item"""
        return item in self.inventory

    def use_item(self, item):
        """Use item from inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False

    def change_health(self, amount):
        """Change health points"""
        self.health += amount
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0