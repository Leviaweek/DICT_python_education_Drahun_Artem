"""Card class module"""
from __future__ import annotations

class Card:
    """User card"""
    def __init__(self, number: str, pin_code: int, balance: int):
        self.number = number
        self.__pin_code = pin_code
        self.__balance = balance

    def EqPinCode(self, other: int) -> bool:
        """Equal pincodes

        Args:
            other (int): other pin-code

        Returns:
            bool: equal result
        """
        return self.__pin_code == other

    def add_income(self, income: int) -> None:
        """Add income to balance

        Args:
            income (int): income
        """
        self.__balance += income
    
    def get_balance(self) -> int:
        """Get card balance

        Returns:
            int: balance
        """
        return self.__balance

    def transfer(self, other: Card, amount: int) -> None:
        """Do transfer with other card

        Args:
            other (Card): other card
            amount (int): sum for transfer
        """
        self.__balance -= amount
        other.add_income(amount)
