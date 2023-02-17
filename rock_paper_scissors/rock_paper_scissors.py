"""Main file"""
from game_menu import GameMenu

def main() -> None:
    """Main function"""
    game = GameMenu()
    game.login()
    try:
        while True:
            game.main_menu()
    except KeyboardInterrupt:
        print("Exiting...")
    print("Goodbye")

if __name__ == "__main__":
    main()
