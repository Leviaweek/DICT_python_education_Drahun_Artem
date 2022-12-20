"""It's my credit calculator"""
from argparse import ArgumentParser
import math
class Calculator:
    """Credit calculator class"""
    def __init__(self):
        self.parser = ArgumentParser(
            description="Credit calculator")
        self.parser.add_argument("--type", choices=["annuity", "diff"],
                                 required=True, help="annuity or diff",
                                 type=str)
        self.parser.add_argument(
            "--payment", help="monthly payment", type=float)
        self.parser.add_argument(
            "--principal", help="loan principal", type=float)
        self.parser.add_argument(
            "--periods", help="number of months", type=int)
        self.parser.add_argument(
            "--interest", help="interest", type=float, required=True)
        self.args = self.parser.parse_args()
        self.nominal_interest = self.args.interest / 100
        self.principal = self.args.principal
        self.periods = self.args.periods
        self.payment = self.args.payment
        self.type = self.args.type

    def main_menu(self) -> None:
        """credit calculator menu"""
        if self.type == "diff":
            self.diff_calc()
        elif self.type == "annuity":
            self.annuity_calc()

    def diff_calc(self) -> None:
        """Differencial calculating method"""
        overpayment = 0
        if self.principal is None or self.periods is None or self.payment is not None:
            print("Incorrect")
            return
        for i in range(self.periods):
            diff = ((self.principal/self.periods) + self.nominal_interest * (self.principal -
            ((self.principal * i)/self.periods)))
            diff = math.ceil(diff)
            print(f"Month {i+1}: payment is {diff}")
            overpayment += diff
        print(f"Overpayment: {overpayment - int(self.principal)}")

    def annuity_calc(self) -> None:
        """Annuity calculating method"""
        overpayment = 0
        if self.payment is None and self.principal > 0:
            annuity = (self.principal * ((self.nominal_interest *
            math.pow((1 + self.nominal_interest), self.periods))
            / (math.pow((1 + self.nominal_interest), self.periods) - 1)))
            annuity = math.ceil(annuity)
            overpayment = annuity * self.periods - self.principal
            print(f"You annuity payment = {annuity}!")
            print(f"Overpayment = {int(overpayment)}")
        elif self.principal is None and self.payment > 0:
            self.principal = ((self.payment) / ((self.nominal_interest
            * math.pow((1 + self.nominal_interest), self.periods))
            / (math.pow((1 + self.nominal_interest), self.periods) - 1)))
            overpayment = math.ceil((self.payment * self.periods) - self.principal)
            self.principal = math.ceil(self.principal)
            print(f"Your loan principal = {self.principal}!")
            print(f"Overpayment = {int(overpayment)}")
        else:
            print("Incorrect input")
