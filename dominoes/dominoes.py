"""Dominoes main file"""
from game_ui import GameUI

def main() -> None:
    """Main function"""
    game_ui = GameUI()
    try:
        while True:
            game_ui.game_menu()
    except KeyboardInterrupt:
        print("Goodbye!")

if __name__ == '__main__':
    main()
