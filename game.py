import os
from player import Player
from locations import locations
from actions import Actions


class Game:
    def __init__(self):
        self.player = Player()
        self.actions = Actions(self)

    def start(self):
        """Start the game"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to Forest Adventure!")
        name = input("Please enter your name: ")
        self.player.name = name
        self.player.location = "forest"

        print(f"\nHello, {name}! Your adventure begins!")
        input("Press Enter to continue...")

        self.game_loop()

    def game_loop(self):
        """Main game loop"""
        while True:
            self.show_status()
            self.show_location()

            choice = input("\nPlease select (enter number): ")

            if choice == "0":
                if self.confirm("Are you sure you want to quit?"):
                    break
            else:
                self.handle_choice(choice)

            # Check if game is over
            if self.check_game_end():
                break

    def show_status(self):
        """Display player status"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print(f"Player: {self.player.name} | Health: {self.player.health}")
        print(f"Items: {', '.join(self.player.inventory) if self.player.inventory else 'None'}")
        print("=" * 50)

    def show_location(self):
        """Display current location"""
        loc = locations[self.player.location]
        print(f"\n【{loc['name']}】")
        print(loc['description'])
        print("\nYou can:")

        for key, option in loc['options'].items():
            print(f"{key}. {option['text']}")
        print("0. Quit Game")

    def handle_choice(self, choice):
        """Handle player choice"""
        loc = locations[self.player.location]

        if choice in loc['options']:
            option = loc['options'][choice]

            if 'location' in option:
                # Move to new location
                self.player.location = option['location']
            elif 'action' in option:
                # Execute action
                action_name = option['action']
                if hasattr(self.actions, action_name):
                    getattr(self.actions, action_name)()
        else:
            print("Invalid choice!")
            input("Press Enter to continue...")

    def check_game_end(self):
        """Check if game is over"""
        if self.player.health <= 0:
            print("\nYour health has reached zero! Game Over!")
            input("Press Enter to return to main menu...")
            return True

        if "Treasure" in self.player.inventory:
            print("\nCongratulations! You found the treasure! You Win!")
            print(f"Final status: Health {self.player.health}, Items {len(self.player.inventory)}")
            input("Press Enter to return to main menu...")
            return True

        return False

    def confirm(self, message):
        """Confirm action"""
        while True:
            response = input(f"{message} (y/n): ").lower()
            if response == 'y':
                return True
            elif response == 'n':
                return False
            else:
                print("Please enter y or n")