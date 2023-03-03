"""Game state file"""
from enum import Enum

class GameState(Enum):
    """Game state enum"""
    NOT_STARTED = 0
    PLAYER_MOVE = 1
    BOT_MOVE = 2
    PLAYER_WIN = 3
    BOT_WIN = 4
    FISH = 5
    DRAW = 6
