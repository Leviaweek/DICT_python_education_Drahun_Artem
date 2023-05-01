"""Banking system module"""
from data_base import DataBase
from card import Card

class BankingSystem:
    """Banking system with requests to database"""
    def __init__(self):
        self.data_base = DataBase()

    def check_card_number(self, card_number: str) -> bool:
        """Check card number in database

        Args:
            card_number (str): user card number

        Returns:
            bool: true or false, card in base or not
        """
        self.data_base.cursor.execute(f"SELECT number FROM card WHERE number = {card_number};")
        if not self.data_base.cursor.fetchone():
            return False
        return True

    def add_account(self, card_number: str, pin_code: int) -> None:
        """Create account in table
        Args:
            card_number (str): user card number
            pin_code (int): user new pin code
        """
        self.data_base.cursor.execute(f"INSERT INTO card (number, pin) VALUES ({card_number}, {pin_code});")
        self.data_base.connecting.commit()
    
    def get_card(self, card_number: str) -> Card:
        """Get card frm table

        Args:
            card_number (str): user card number

        Returns:
            Card: user card
        """
        self.data_base.cursor.execute(f"SELECT * FROM card WHERE number = {card_number};")
        data = self.data_base.cursor.fetchone()
        return Card(data[1], data[2], data[3])

    def delete_account(self, card_number: str) -> None:
        """Delete user account from table

        Args:
            card_number (str): user card number
        """
        self.data_base.cursor.execute(f"DELETE FROM card WHERE number = {card_number};")
        self.data_base.connecting.commit()
    
    def update_account(self, card: Card) -> None:
        """Update user balance

        Args:
            card (Card): user card
        """
        self.data_base.cursor.execute(f"UPDATE card SET balance = {card.get_balance()} WHERE number = {card.number};")
        self.data_base.connecting.commit()
