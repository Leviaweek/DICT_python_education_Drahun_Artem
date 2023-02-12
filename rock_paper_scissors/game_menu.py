"""Game menu class module"""
import random
import sys
from game_core import GameCore

class GameMenu:
    """Game menu class"""
    ALL_CHOICES = ["Rock", "Fire", "Scissors", "Snake", "Human", "Tree", "Wolf",
    "Sponge", "Paper", "Air", "Water", "Dragon", "Devil", "Lightning", "Gun"]

    def __init__(self) -> None:
        self.game_core = GameCore()
        self.score = 0
        self.scoreboard = {}
        self.name = "Unknown"

    def login(self) -> None:
        """User login to game"""
        print("It's a game \"Rock-Paper-Scissors\"")
        user_name = input("Enter your name: ")
        if user_name.strip() != "":
            self.name = user_name
        self.read_score_file()
        print(f"Hi, {self.name}")
        print(f"Your score: {self.score}")

    def main_menu(self) -> None:
        """User choose game mode"""
        while True:
            print("Choose game mode: 1. Full, 2. Classic, 3. User")
            user_choice = input(">>> ").title()
            match user_choice:
                case "1" | "Full":
                    self.full_game()
                case "2" | "Classic":
                    self.classic_game()
                case "3" | "User":
                    self.custom_game()
                case _:
                    print("Incorrect input")
                    continue
            break
        self.start_game()

    def start_game(self) -> None:
        """Start game process"""
        while True:
            try:
                self.print_all_options(self.game_core.game_options)
                user_input = input(">>> ").strip().lower()
                if user_input == "!exit":
                    self.scoreboard[self.name] = self.score
                    self.write_score_file()
                    print("Bye!")
                    sys.exit(0)
                user_input = user_input.title()
                if user_input.isnumeric():
                    user_choice = self.game_core.game_options[int(user_input) - 1]
                elif user_input in self.game_core.game_options:
                    user_choice = user_input
                else:
                    raise ValueError
                bot_choice = random.choice(self.game_core.game_options)
                result = self.game_core.game_round(user_choice, bot_choice)
                print(self.round_result(result, user_choice, bot_choice))
                self.score += result
                print(f"Your score: {self.score}")
            except IndexError:
                print("Unknown number")
            except ValueError:
                print("Unknown option")

    @staticmethod
    def round_result(result: int, user_choice: str, bot_choice: str) -> str:
        """Print round result with number

        Args:
            result (int): added score
            user_choice (str): user option
            bot_choice (str): bot option

        Returns:
            str: round text
        """
        if result == 0:
            return f"I win. I choose {bot_choice}, you choose {user_choice}"
        elif result == 50:
            return f"Draw. We choose {user_choice}"
        else:
            return f"You win. I choose {bot_choice}, you choose {user_choice}"

    def full_game(self) -> None:
        """User choose full game"""
        self.game_core.game_options = self.ALL_CHOICES

    def classic_game(self) -> None:
        """User choose classic game"""
        self.game_core.game_options = ["Rock", "Scissors", "Paper"]

    def custom_game(self) -> None:
        """User choose custom game"""
        self.print_all_options(self.ALL_CHOICES)
        print("Your choice must be greater than three and odd")
        while True:
            try:
                user_choice = input(">>> ")
                splitted = user_choice.split(",")
                for i in self.ALL_CHOICES:
                    for j in splitted:
                        if i == j.title():
                            self.game_core.game_options.append(j.title())
                        if len(splitted) < 3 or len(splitted) % 2 == 0:
                            raise ValueError
                break
            except ValueError:
                print("Invalid input!")
                continue

    @staticmethod
    def print_all_options(options: list[str]) -> None:
        """Method for print all options

        Args:
            options (list[str]): list with all options
        """
        print("Choose options from this list: ")
        for i, value in enumerate(options):
            print(f"{i + 1}. {value}".ljust(15), end="")
            if (i + 1) % 3 == 0:
                print()
        print()

    def read_score_file(self) -> None:
        """Read score from file."""
        with open("results.csv", "a+", encoding="utf-8") as file:
            lines = file.readlines()
            for i in lines:
                text = i.split(",")
                self.scoreboard[text[0]] = text[1]
            if self.name == "Unknown":
                return
            if self.name in self.scoreboard:
                self.score += int(self.scoreboard[self.name])
            else:
                self.scoreboard[self.name] = self.score

    def write_score_file(self) -> None:
        """Write score to file."""
        with open("results.csv", "w", encoding="utf-8") as file:
            for key, value in self.scoreboard.items():
                file.write(f"\"{key}\", \"{value}\"\n")
