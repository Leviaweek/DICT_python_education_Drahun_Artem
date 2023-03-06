import json
import requests
from os import path

class CurrencyExchange:
    """Currency exchange class"""

    def __init__(self) -> None:
        """Constructor"""
        self.base_currency = ""
        self.cached_rates = {}

    def currency_menu(self) -> None:
        """Main menu"""
        self.base_currency = input("Please enter the base currency: ").lower()
        self.__get_cached_rates()
        if self.base_currency in self.cached_rates:
            print("This currency is in the cache")
        else:
            print("This currency is not in the cache")
            self.__get_rates_from_api(self.base_currency)
        while True:
            currency_for_exchange = input("Please enter the currency you want to exchange: ").lower()
            try:
                amount = float(input("Please enter the amount: "))
            except ValueError:
                print("Invalid amount")
                continue

            currency = self.cached_rates[self.base_currency][currency_for_exchange]["rate"]
            result = round(amount * currency, 2)
            print(f"{amount} {self.base_currency} is {amount * currency} {currency_for_exchange}")

    def __get_rates_from_file(self, name) -> dict:
        """load rates from file

        Args:
            name (str): filename

        Returns:
            dict(): rates
        """
        with open(name, "r") as file:
            return json.load(file)

    def __get_rates_from_api(self) -> None:
        """Get rates from floatrates"""
        url = f"http://www.floatrates.com/daily/{self.base_currency}.json"
        response = requests.get(url)
        if response.status_code == 200:
            rates = response.json()
            self.cached_rates[self.base_currency] = rates
            with open("cache.json", "w") as file:
                json.dump(self.cached_rates, file)
        else:
            raise ValueError("Invalid currency code")

    def __get_cached_rates(self) -> None:
        """Load cache to variable"""
        if path.exists("cache.json"):
            self.cached_rates = self.__get_rates_from_file("cache.json")
