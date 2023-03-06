"""Main file for currency exchange app"""
from currency_exchange import CurrencyExchange

def main():
    """Main function"""
    try:
        while True:
            try:
                currency_exchange = CurrencyExchange()
                currency_exchange.currency_menu()
            except ValueError as error:
                print(error)
    except KeyError:
        print("Invaild currency")
    except KeyboardInterrupt:
        print("Goodbye!")

if __name__ == "__main__":
    main()
