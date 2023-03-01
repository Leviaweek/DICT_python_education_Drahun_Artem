"""Game board file"""
from dominoe import Dominoe

class GameBoard:
    """Game board class"""
    def __init__(self) -> None:
        """Constructor"""
        self.board = []

    def __str__(self) -> str:
        """Generate string with game board

        Returns:
            str: game board in str
        """
        if len(self.board) <= 6:
            return "".join(map(str, self.board))
        return "".join(map(str, self.board[:3])) + "..." + "".join(map(str, self.board[-3:]))

    def __len__(self) -> int:
        """Game board length

        Returns:
            int: board length
        """
        return len(self.board)

    def __iter__(self) -> iter:
        """Game board iterator

        Returns:
            iter: iterator
        """
        return iter(self.board)

    def __getitem__(self, index: int) -> Dominoe:
        """Get item from game board

        Args:
            index (int): item index

        Returns:
            Dominoe: dominoe object
        """
        return self.board[index]

    def add_right(self, dominoe: Dominoe) -> bool:
        """add dominoe to game board right side

        Args:
            dominoe (Dominoe): dominoe object

        Returns:
            bool: result of adding
        """
        if dominoe.left == self.board[-1].right:
            self.board.append(dominoe)
            return True
        if dominoe.right == self.board[-1].right:
            dominoe.invert()
            self.board.append(dominoe)
            return True
        return False

    def add_left(self, dominoe: Dominoe) -> bool:
        """add dominoe to game board left side

        Args:
            dominoe (Dominoe): dominoe object

        Returns:
            bool: result of adding
        """
        if dominoe.right == self.board[0].left:
            self.board.insert(0, dominoe)
            return True
        if dominoe.left == self.board[0].left:
            dominoe.invert()
            self.board.insert(0, dominoe)
            return True
        return False
