"""Main module"""
from banking_ui import BankingUi

def main() -> None:
    """Main function"""
    ui = BankingUi()
    ui.loop()

if __name__ == "__main__":
    main()