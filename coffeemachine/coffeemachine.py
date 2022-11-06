"""It's my coffeemachine :)"""

class Machine:
    """Coffeemachine class"""
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.action = "Waiting for action"

    def print_interface(self):
        """Printing"""
        if self.action == "Waiting for action":
            print("Write action(buy, fill, take, remaining, exit)")
        elif self.action == "Coffee selecting":
            print("What do you want to buy?")
            print("1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
        elif self.action == "Waiting for water":
            print("Enter the amount of water(maximum = 50000):")
        elif self.action == "Waiting for milk":
            print("Enter the amount of milk(maximum = 10000)")
        elif self.action == "Waiting for beans":
            print("Enter the amount of beans(maximum = 10000)")
        elif self.action == "Waiting for cups":
            print("Enter the amount of cups(maximum = 1000)")

    def espresso(self):
        """Espresso"""
        self.action = "Making coffee"
        print("Checking resources...")
        water_count = 250
        beans_count = 16
        money_cost = 4
        if (self.water >= water_count
        and self.beans >= beans_count):
            print("I have enough resources for Espresso")
            self.water -= water_count
            self.beans -= beans_count
            self.money += money_cost
            self.cups -= 1
            print("Done!")
        else:
            print("I don't have resources for Espresso :(")
        self.action = "Waiting for action"

    def latte(self):
        """making latte"""
        self.action = "Making coffee"
        print("Checking resources...")
        water_count = 350
        beans_count = 20
        milk_count = 75
        money_cost = 7
        if (self.water >= water_count
        and self.beans >= beans_count
        and self.milk >= 75):
            print("I have enough resources for latte")
            self.water -= water_count
            self.beans -= beans_count
            self.milk -= milk_count
            self.money += money_cost
            self.cups -= 1
            print("Done!")
        else:
            print("I don't have resources for latte :(")
        self.action = "Waiting for action"

    def cappucino(self):
        """making cappucino"""
        self.action = "Making coffee"
        print("Checking resources...")
        water_count = 200
        beans_count = 12
        milk_count = 100
        money_cost = 6
        if (self.water >= water_count
        and self.beans >= beans_count
        and self.milk >= milk_count):
            print("I have enough resources for cappucino")
            self.water -= water_count
            self.beans -= beans_count
            self.milk -= milk_count
            self.money += money_cost
            self.cups -= 1
            print("Done!")
        else:
            print("I don't have resources for cappucino :(")
        self.action = "Waiting for action"

    def take(self):
        """taking money"""
        print(f"I gave you {self.money}")
        self.money = 0

    def remaining(self):
        """Print all resources"""
        print(f"""The coffeemachine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money""")

    def fill(self, user_input:int):
        """Filling"""
        if self.action == "Waiting for water":
            try:
                user_input = int(user_input)
                if user_input < 1 or (user_input+self.water) > 50000:
                    raise ValueError
                self.water += user_input
                self.action = "Waiting for milk"
            except ValueError:
                print("Incorrect input")
        elif self.action == "Waiting for milk":
            try:
                user_input = int(user_input)
                if user_input < 1 or (user_input+self.milk) > 10000:
                    raise ValueError
                self.milk += user_input
                self.action = "Waiting for beans"
            except ValueError:
                print("Incorrect input")
        elif self.action == "Waiting for beans":
            try:
                user_input = int(user_input)
                if user_input < 1 or (user_input+self.beans) > 10000:
                    raise ValueError
                self.beans += user_input
                self.action = "Waiting for cups"
            except ValueError:
                print("Incorrect input")
        elif self.action == "Waiting for cups":
            try:
                user_input = int(user_input)
                if user_input < 1 or (user_input+self.cups) > 1000:
                    raise ValueError
                self.cups += user_input
                self.action = "Waiting for action"
            except ValueError:
                print("Incorrect input")

    def input_method(self, user_input):
        """Input"""
        if user_input == "buy" and self.action == "Waiting for action":
            self.action = "Coffee selecting"
        elif user_input == "back":
            self.action = "Waiting for action"
        elif user_input == "1" and self.action == "Coffee selecting":
            self.espresso()
        elif user_input == "2" and self.action == "Coffee selecting":
            self.latte()
        elif user_input == "3" and self.action == "Coffee selecting":
            self.cappucino()
        elif user_input == "fill" and self.action == "Waiting for action":
            self.action = "Waiting for water"
        elif self.action in ("Waiting for milk", "Waiting for water",
           "Waiting for beans", "Waiting for cups"):
            self.fill(user_input)
        elif user_input == "take" and self.action == "Waiting for action":
            self.take()
        elif user_input == "remaining" and self.action == "Waiting for action":
            self.remaining()
        elif user_input == "exit" and self.action == "Waiting for action":
            self.action = "Exiting"
        else:
            print("Unknown command")

def main():
    """coffeemachine main function"""
    print("\t\tCOFFEEMACHINE\n\n")
    coffeemachine = Machine()
    while True:
        coffeemachine.print_interface()
        user_input = input("> ")
        coffeemachine.input_method(user_input.lower())
        if coffeemachine.action == "Exiting":
            break
    print("Goodbye...")

if __name__ == "__main__":
    main()
