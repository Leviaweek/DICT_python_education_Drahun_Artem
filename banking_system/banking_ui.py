"""Banking UI module"""
import random
from system import BankingSystem
from ui_state import UiState
from account import Account
from card import Card

class BankingUi:

    def __init__(self):
        self.__state = UiState.NotLoggined
        self.__banking_system = BankingSystem()
        self.__user_exit = False
        self.__account = None

    def loop(self) -> None:
        """Ui loop"""
        while True:
            self.print_menu()

            try:
                user_choice = int(input("Choose number: "))
            except ValueError:
                print("Input only numbers")
                continue

            self.__user_choice(user_choice)

            if self.__user_exit:
                return

    def __user_choice(self, choice: int) -> None:
        """User choose from menu
        
        Args: 
            choice (int): number in menu
        """
        match (self.__state):
            case UiState.NotLoggined:
                match (choice):
                    case 1:
                        self.__create_account()
                    case 2:
                        self.__login()
                    case 0:
                        self.__user_exit = True
                    case _:
                        print("Incorrect input")
            case UiState.Loggined:
                match(choice):
                    case 1:
                        print(f"Your balance: {self.__account.card.get_balance()}")
                    case 2:
                        income = self.__input_income()
                        self.__account.card.add_income(income)
                        self.__banking_system.update_account(self.__account.card)
                    case 3:
                        self.__do_transfer()
                    case 4:
                        self.__close_account()
                        self.__log_out()
                    case 5:
                        self.__log_out()
                    case 0:
                        self.__user_exit = True
                    case _:
                        print("Incorrect input")

    def __input_income(self) -> int:
        """Input sum
        
        Returns:
        (int) money"""
        while True:
            try:
                income = int(input("Enter income: "))
                if income <= 0:
                    raise ValueError
                return income
            except ValueError:
                print("Input only positive numbers")
                continue

    def __log_out(self) -> None:
        """Log out"""
        self.__account = None
        self.__state = UiState.NotLoggined

    def __close_account(self) -> None:
        """Delete account"""
        self.__banking_system.delete_account(self.__account.card.number)

    def __do_transfer(self) -> None:
        """Do transfer"""
        while True:
            print("Transfer")
            card_number = input("Enter card number: ")
            if card_number == self.__account.card.number:
                print("You can't transfer money to the same account!")
                break

            if not self.__banking_system.check_card_number(card_number):
                print("Such a card does not exist.")
                return
            
            card = self.__banking_system.get_card(card_number)

            money = self.__input_income()
            if money > self.__account.card.get_balance():
                print("Not enough money!")
                break

            self.__account.card.transfer(card, money)
            break
        print(f"Balance: {self.__account.card.get_balance()}")
        self.__banking_system.update_account(self.__account.card)
        self.__banking_system.update_account(card)

    def __create_account(self) -> None:
        """Create new account"""
        card_number = self.__generate_card_number()
        pin = self.__generate_pin()
        print(f"Your card has been created\nYour card number:\n{card_number}\nYour card PIN:\n{pin}")
        self.__banking_system.add_account(card_number, pin)
        card = Card(card_number, pin, 0)
        self.__account = Account(card)
        self.__state = UiState.Loggined

    def __generate_card_number(self) -> str:
        """Generate card number

        Returns:
            str: card number
        """
        while True:
            card_number = "400000"
            for _ in range(9):
                card_number += str(random.randint(0, 9))
            
            card_number += self.__generate_luhn(card_number)
            if not self.__banking_system.check_card_number(card_number) == None:
                return card_number

    def __generate_pin(self) -> int:
        """Generate pin-code
        
        Returns:
            int: pin-code
        """
        return random.randint(0000, 9999)

    def __generate_luhn(self, card_number: str) -> str:
        """generate last luhn number

        Args:
            card_number (str): card number without 1 number

        Returns:
            str: luhn number
        """
        numbers = [int(i) for i in card_number]

        for i in range(len(card_number)):
            if i % 2 != 0:
                numbers[i] *= 2
            if numbers[i] > 9:
                numbers[i] -= 9
        number = sum(numbers) % 10
        return str(number)

    def __login(self) -> None:
        """Login user"""
        card_number = input("Enter your card number: ")
        if not self.__banking_system.check_card_number(card_number):
            print("Wrong card number")
            return
        card = self.__banking_system.get_card(card_number)
        pin_code = input("Enter your PIN: ")
        if not card.EqPinCode(pin_code):
            print("Wrong PIN!")
            return
        self.__account = Account(card)
        self.__state = UiState.Loggined
        print("Login succesful")

    def print_menu(self):
        """Print user interface menu"""
        match (self.__state):
            case UiState.NotLoggined:
                print("""1. Create an account
2. Log into account
0. Exit""")
            case UiState.Loggined:
                print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")
