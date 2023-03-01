"""Domenoe class"""
class Dominoe:
    """Dominoe class"""

    def __init__(self, left: int, right: int) -> None:
        """Constructor

        Args:
            left (int): left dice number
            right (int): right dice number
        """
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """Generate string with dice

        Returns:
            str: dice in str
        """
        return f"[{self.left}|{self.right}]"

    def __contains__(self, item: object) -> bool:
        """Check item in dice

        Args:
            item (obj): item for check in dice

        Returns:
            bool: comprassion result 
        """
        return item in (self.left, self.right)

    def __iter__(self) -> iter:
        """Iterate over dice

        Returns:
            iter: iterator
        """
        return iter((self.left, self.right))

    def invert(self) -> None:
        """Invert dominoe dice"""
        self.left, self.right = self.right, self.left

    @property
    def is_duble(self) -> bool:
        """Check if dice is duble

        Returns:
            bool: dice is duble
        """
        return self.left == self.right

    @property
    def dice_cost(self) -> int:
        """Dice cost

        Returns:
            int: sum of dice
        """
        return self.left + self.right
