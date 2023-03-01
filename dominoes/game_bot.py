"""GameBot class file"""
from user import User
from dominoe import Dominoe
from move import Move

class GameBot(User):
    """GameBot class"""

    def calculate_move(self) -> bool:
        """Calculate bot move

        Returns:
            bool: can bot move
        """
        dice_rate = {}
        dices = {}
        for i in self.game_board.board + self.dices:
            if i.left in dice_rate:
                dice_rate[i.left] += 1
            else:
                dice_rate[i.left] = 1
            if i.right in dice_rate:
                dice_rate[i.right] += 1
            else:
                dice_rate[i.right] = 1
        for _, dice in enumerate(self.dices):
            dices[dice] = dice_rate[dice.left] + dice_rate[dice.right]
        for _, _ in enumerate(self.dices):
            dice = self.__choose_max_dice(dices)
            if(dice.right == self.game_board[-1].right
               or dice.left == self.game_board[-1].right):
                self.try_move(self.dices.index(dice), Move.RIGHT)
                return True
            elif(dice.right == self.game_board[0].left
                or dice.left == self.game_board[0].left):
                self.try_move(self.dices.index(dice), Move.LEFT)
                return True
            dices.pop(dice)
        return False

    def __choose_max_dice(self, dices: dict) -> Dominoe:
        """Choose max dice from dict

        Args:
            dices (dict{Dominoe: int}): dices with rate

        Returns:
            Dominoe: dice with max rate
        """
        max_dice = None
        for dice, _ in dices.items():
            if max_dice is None or dices[dice] > dices[max_dice]:
                max_dice = dice
        return max_dice
