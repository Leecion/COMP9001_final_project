import os
from game import Game

def main_menu():
    """Display main menu"""
    game = Game()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 24)
        print("    Forest Adventure")
        print("=" * 24)
        print("1. Start Game")
        print("2. Game Instructions")
        print("3. Exit")
        
        choice = input("\nPlease select: ")
        
        if choice == "1":
            game.start()
        elif choice == "2":
            show_instructions()
        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")

def show_instructions():
    """Display game instructions"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 40)
    print("    Game Instructions")
    print("=" * 40)
    print("This is a simple text adventure game.")
    print("You need to explore the forest, collect items, and find the treasure.")
    print("Enter numbers to choose your actions.")
    print("Good luck!")
    input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main_menu()
