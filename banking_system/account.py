"""Account module"""
from dataclasses import dataclass
from card import Card

@dataclass
class Account:
    """User account"""
    card: Card
