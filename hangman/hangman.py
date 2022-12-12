"""Game class file"""
import random
import enum

class GameState(enum.Enum):
    """Hangman gamestate"""
    GAME_MOVE = 1
    GAME_WIN = 2
    GAME_LOSE = 3

class HangMan:
    """Hangman class"""

    def __init__(self):
        self.words = ["python", "javascript", "programming", "interpreter", "compiler"]
        self.game_state = GameState.GAME_MOVE
        self.closed_word = []
        self.user_letter = ""
        self.game_word = ""
        self.used_letters = set()
        self.mistakes = 0

    def game_state_creating(self) -> None:
        """Creating game state"""
        self.game_state = GameState.GAME_MOVE

    def closed_word_creating(self) -> None:
        """Creating closed word"""
        self.closed_word = list("*" * len(self.game_word))

    def game_word_creating(self) -> None:
        """Creating game word"""
        self.game_word = random.choice(self.words)

    def used_letters_creating(self) -> None:
        """Creating used letters set"""
        self.used_letters = set()

    def mistakes_creating(self) -> None:
        """Setting mistakes"""
        self.mistakes = 0

    def printer(self) -> None:
        """Print main method"""
        print(f"{self.mistakes} mistakes")
        print("".join(self.closed_word))

    def inputing(self) -> None:
        """All user inputs"""
        while True:
            self.user_letter = input(">>> ").lower()
            if self.user_letter > 'z' or self.user_letter < 'a':
                print("Input only english letters!")
                continue
            if len(self.user_letter) == 1 or len(self.user_letter) == len(self.game_word):
                break
            print("input only number or full word")

    def user_move(self) -> None:
        """User move and check method"""
        if len(self.user_letter) != 1:
            if self.user_letter == self.game_word:
                self.game_state = GameState.GAME_WIN
                return
            self.game_state = GameState.GAME_LOSE

        if self.user_letter in self.used_letters:
            print("You use this letter")
            return

        self.used_letters.add(self.user_letter)

        if self.user_letter in self.game_word:
            for i, _ in enumerate(self.game_word):
                if self.user_letter == self.game_word[i]:
                    self.closed_word[i] = self.game_word[i]
        else:
            print("Mistake!")
            self.mistakes += 1
            return

        if self.mistakes == 8:
            self.game_state = GameState.GAME_LOSE
            return

        if "".join(self.closed_word) == self.game_word:
            self.game_state = GameState.GAME_WIN

    def game_loop(self) -> None:
        """Game looping"""
        self.game_word_creating()
        self.closed_word_creating()
        self.mistakes_creating()
        self.game_state_creating()
        self.used_letters_creating()
        while True:
            self.printer()
            self.inputing()
            self.user_move()
            match self.game_state:
                case GameState.GAME_WIN:
                    print(f"You win! Word is {self.game_word}")
                    return
                case GameState.GAME_LOSE:
                    print(f"You lose! Word is {self.game_word}")
                    return

    def game_menu(self) -> None:
        """Game main menu"""
        print("\t\tHANGMAN")
        while True:
            try:
                print("Type \"play\" to play the game, \"exit\" to quit:")
                user_input = input(">>> ").lower()
                if user_input == "play":
                    self.game_loop()
                elif user_input == "exit":
                    print("Goodbye")
                    return
                else:
                    print("Incorrect input")
            except KeyboardInterrupt:
                print("Ok, goodbye")
                return
