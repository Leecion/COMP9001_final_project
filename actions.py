import random


class Actions:
    def __init__(self, game):
        self.game = game

    def search_forest(self):
        """Search the forest"""
        print("\nYou carefully search the forest entrance...")

        if not self.game.player.has_item("Torch"):
            print("You found a torch!")
            self.game.player.add_item("Torch")
        else:
            print("You didn't find anything new.")

        input("Press Enter to continue...")

    def drink_water(self):
        """Drink water and rest"""
        print("\nYou drink the clear stream water and feel much better!")
        self.game.player.change_health(20)
        print(f"You recovered 20 health points! Current health: {self.game.player.health}")
        input("Press Enter to continue...")

    def search_stream(self):
        """Search around the stream"""
        print("\nYou search carefully around the stream...")

        if not self.game.player.has_item("Key"):
            print("You found a rusty key in the water!")
            self.game.player.add_item("Key")
        else:
            print("There's nothing else in the stream.")

        input("Press Enter to continue...")

    def explore_cave(self):
        """Explore the cave"""
        print("\nYou carefully walk deeper into the cave...")

        if self.game.player.has_item("Torch"):
            print("The torch lights the way! You discovered a hidden room!")
            self.game.player.location = "treasure_room"
        else:
            print("It's too dark! You tripped over a rock!")
            self.game.player.change_health(-10)
            print(f"You lost 10 health points! Current health: {self.game.player.health}")

        input("Press Enter to continue...")

    def open_treasure(self):
        """Open the treasure chest"""
        print("\nYou approach the treasure chest...")

        if self.game.player.has_item("Key"):
            print("You opened the chest with the key!")
            print("It's filled with gold coins and jewels!")
            self.game.player.add_item("Treasure")
            print("You obtained the treasure! Congratulations on completing your adventure!")
        else:
            print("The chest is locked! You need a key.")

        input("Press Enter to continue...")