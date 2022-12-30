"""Class for all coffee types"""
from dataclasses import dataclass

@dataclass
class Coffee:
    """Class with types coffee"""
    water: int
    milk: int
    beans: int
    cost: int
    name: str
