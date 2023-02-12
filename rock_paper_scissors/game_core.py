"""rock_paper_scissors class module."""

class GameCore:
    """RockPaperScissors class."""

    def __init__(self):
        self.game_options = []

    def game_round(self, user_choice: str, bot_choice: str) -> int:
        """Calculate winner"

        Args:
            user_choice (str): user option
            bot_choice (str): bot option

        Returns:
            int: added score
        """
        user_id = self.game_options.index(user_choice)
        bot_id = self.game_options.index(bot_choice)
        win_distance = len(self.game_options) // 2
        distance = self.calculate_distance(user_id, bot_id)
        if distance == 0:
            return 50
        if distance <= win_distance:
            return 100
        return 0

    def calculate_distance(self, first_id: int, second_id: int) -> int:
        """Calculate distance two players

        Args:
            first_id (int): first player option position
            second_id (int): second player option position

        Returns:
            int: result distance
        """
        distance = first_id - second_id
        if distance < 0:
            distance += len(self.game_options)
        return distance
