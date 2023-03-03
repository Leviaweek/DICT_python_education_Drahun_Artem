"""GameCore file"""
import random
from dominoe import Dominoe
from game_state import GameState
from game_board import GameBoard
from game_bot import GameBot
from game_player import Player

class GameCore():
    """GameCore class"""
    def __init__(self) -> None:
        """Constructor"""
        self.stock_dices = []
        self.game_board = GameBoard()
        self.player = Player(self.game_board)
        self.bot = GameBot(self.game_board)
        self.game_state = GameState.NOT_STARTED

    def load_game(self) -> None:
        """Load game"""
        self.stock_dices = []
        self.game_board = GameBoard()
        self.player = Player(self.game_board)
        self.bot = GameBot(self.game_board)
        self.game_state = GameState.NOT_STARTED
        for i in range(7):
            for j in range(i, 7):
                self.stock_dices.append(Dominoe(i, j))

    def skip_or_take(self, dices) -> None:
        """Skip or take"""
        for i in dices:
            if ((i.right == self.game_board[0].left or i.left == self.game_board[0].left)
                or i.right == self.game_board[-1].right or i.left == self.game_board[-1].right):
                raise ValueError("You can't skip")
        if len(self.stock_dices) != 0:
            if self.game_state == GameState.PLAYER_MOVE:
                self.player.dices.append(random.choice(self.stock_dices))
                self.stock_dices.remove(self.player.dices[-1])
                self.game_state = GameState.BOT_MOVE
            elif self.game_state == GameState.BOT_MOVE:
                self.bot.dices.append(random.choice(self.stock_dices))
                self.stock_dices.remove(self.bot.dices[-1])
                self.game_state = GameState.PLAYER_MOVE
            return

    def choose_first_move(self) -> None:
        """Choose who move first"""
        user_dice = self.__choose_max_dice(self.player.dices)
        bot_dice = self.__choose_max_dice(self.bot.dices)
        if ((bot_dice is None and user_dice is not None)
            or user_dice.dice_cost > bot_dice.dice_cost):
            self.game_state = GameState.PLAYER_MOVE
            print("Your move first")
            self.game_board.board.append(user_dice)
            self.player.dices.remove(user_dice)
            self.game_state = GameState.BOT_MOVE
        elif ((user_dice is None and bot_dice is not None)
            or user_dice.dice_cost < bot_dice.dice_cost):
            self.game_state = GameState.BOT_MOVE
            print("My move first")
            self.game_board.board.append(bot_dice)
            self.bot.dices.remove(bot_dice)
            self.game_state = GameState.PLAYER_MOVE

    def choose_dices(self) -> None:
        """Choose dices for bot and player"""
        for _ in range(7):
            dice = random.choice(self.stock_dices)
            self.stock_dices.remove(dice)
            self.player.dices.append(dice)
            dice = random.choice(self.stock_dices)
            self.stock_dices.remove(dice)
            self.bot.dices.append(dice)
        if not any(dice.is_duble for dice in self.player.dices + self.bot.dices):
            raise ValueError

    @staticmethod
    def __choose_max_dice(dices: list) -> Dominoe | None:
        """Choose max dice cost

        Args:
            dices (list): dices list

        Returns:
            Dominoe | None: max dominoe or none
        """
        max_dice = None
        for i in dices:
            if i.is_duble and (max_dice is None or i.dice_cost > max_dice.dice_cost):
                max_dice = i
        return max_dice

    def check_state(self) -> None:
        """Check and change game state"""
        if len(self.player.dices) == 0:
            self.game_state = GameState.PLAYER_WIN
        elif len(self.bot.dices) == 0:
            self.game_state = GameState.BOT_WIN
        elif (self.game_board[-1].right == self.game_board[0].left
        and not any((self.game_board[0].left
                    or self.game_board[0].right in
                    dice for dice in self.player.dices
                    + self.bot.dices
                    + self.stock_dices))):
            self.game_state = GameState.FISH
        self.__change_state()

    def __change_state(self) -> None:
        """Change game state from player move to bot move and vice versa"""
        if self.game_state == GameState.PLAYER_MOVE:
            self.game_state = GameState.BOT_MOVE
        elif self.game_state == GameState.BOT_MOVE:
            self.game_state = GameState.PLAYER_MOVE

    def fish_winner(self) -> None:
        """Calculate winner in fish game state"""
        user_score = self.__dice_sum(self.player.dices)
        bot_score = self.__dice_sum(self.bot.dices)
        if user_score > bot_score:
            self.game_state = GameState.PLAYER_WIN
        elif user_score < bot_score:
            self.game_state = GameState.BOT_WIN
        else:
            self.game_state = GameState.DRAW

    @staticmethod
    def __dice_sum(dices: list) -> int:
        """Sum all dices cost

        Args:
            dices (list(Dominoe)): list dominoe

        Returns:
            int: dice sum
        """
        dice_sum = 0
        for i in dices:
            dice_sum += i.dice_cost
        return dice_sum
