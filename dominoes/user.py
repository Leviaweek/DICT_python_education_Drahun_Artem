"""Abstract base class for user objects."""
from abc import ABC
from game_board import GameBoard
from move import Move

class User(ABC):
    """User abstract class"""
    def __init__(self, game_board: GameBoard) -> None:
        """constructor

        Args:
            game_board (GameBoard): game board object
        """
        self.dices = []
        self.game_board = game_board

    def try_move(self, dice_index, move_direction) -> None:
        """user try move

        Args:
            dice_index (int): dice index
            move_direction (Move): move direction

        Raises:
            ValueError: Invalid move
        """
        if move_direction == Move.RIGHT:
            if self.game_board.add_right(self.dices[dice_index]):
                self.dices.remove(self.dices[dice_index])
                return
        if move_direction == Move.LEFT:
            if self.game_board.add_left(self.dices[dice_index]):
                self.dices.remove(self.dices[dice_index])
                return
        raise ValueError("Invalid move")
