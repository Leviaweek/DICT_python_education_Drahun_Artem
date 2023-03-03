"""GameUI class file"""
import sys
from game_core import GameCore
from game_state import GameState
from move import Move

class GameUI:
    """GameUI class"""
    def __init__(self) -> None:
        """Constructor"""
        self.game_core = GameCore()

    def game_menu(self) -> None:
        """Game menu"""
        print("Do you want start game? (y/n)")
        while True:
            answer = input()
            match answer:
                case "y":
                    self.game_core.load_game()
                    self.game_loop()
                    break
                case "n":
                    print("Goodbye!")
                    sys.exit(0)
                case _:
                    print("Wrong answer. Try again.")

    def game_loop(self) -> None:
        """Game loop"""
        while True:
            try:
                self.game_core.choose_dices()
                break
            except ValueError as error:
                continue
        self.print_game_board()
        self.game_core.choose_first_move()
        while True:
            self.print_game_board()
            match self.game_core.game_state:
                case GameState.PLAYER_MOVE:
                    try:
                        self.user_move_input()
                    except ValueError as error:
                        print(error)
                        continue
                    self.game_core.check_state()
                case GameState.BOT_MOVE:
                    _ = input("Press any key to bot move")
                    if not self.game_core.bot.calculate_move():
                        self.game_core.skip_or_take(self.game_core.bot.dices)
                    self.game_core.check_state()
                case GameState.PLAYER_WIN:
                    print("You win!")
                    return
                case GameState.BOT_WIN:
                    print("I win!")
                    return
                case GameState.FISH:
                    print("Fish!")
                    self.game_core.fish_winner()
                case GameState.DRAW:
                    print("Draw!")
                    return

    def user_move_input(self) -> None:
        """User move input"""
        while True:
            print("Enter your move:")
            answer = input()
            try:
                answer = int(answer)
            except ValueError:
                print("Print only numbers. Try again.")
                continue
            if answer == 0:
                try:
                    self.game_core.skip_or_take(self.game_core.player.dices)
                except ValueError as error:
                    print(error)
                    continue
                break
            if (-len(self.game_core.player.dices) <= answer
                <= len(self.game_core.player.dices)):
                if answer < 0:
                    answer = -answer - 1
                    move_direction = Move.LEFT
                else:
                    answer -= 1
                    move_direction = Move.RIGHT
                self.game_core.player.try_move(answer, move_direction)
                break
            print("Wrong answer. Try again.")

    @property
    def game_state(self) -> str:
        """string game state

        Returns:
            str: game state
        """
        match self.game_core.game_state:
            case GameState.PLAYER_MOVE:
                return "Player move"
            case GameState.BOT_MOVE:
                return "Bot move"
            case GameState.NOT_STARTED:
                return "Not started"
            case GameState.PLAYER_WIN:
                return "Player win"
            case GameState.BOT_WIN:
                return "Bot win"
            case GameState.FISH:
                return "Fish"
            case GameState.DRAW:
                return "Draw"

    @staticmethod
    def __print_dices(dices) -> None:
        """Print dices"""
        print("Your pices: ")
        for ind, dice in enumerate(dices):
            print(f"{ind + 1}:{dice}")

    def print_game_board(self) -> None:
        """Print game board"""
        print(f"""{"=" * 70}
Stock size: {len(self.game_core.stock_dices)}
Computer pieces: {len(self.game_core.bot.dices)}
Game State: {self.game_state}
""")
        self.__print_dices(self.game_core.player.dices)
        print()
        print(self.game_core.game_board)
