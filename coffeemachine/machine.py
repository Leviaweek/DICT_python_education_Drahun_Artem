"""It's my coffeemachine :)"""
import enum
from coffee import Coffee

class MachineState(enum.Enum):
    """All machine states"""
    WAITING_FOR_ACTION = 0
    COFFEE_SELECTING = 1
    MAKING_COFFEE = 2
    WAITING_FOR_WATER = 3
    WAITING_FOR_MILK = 4
    WAITING_FOR_BEANS = 5
    WAITING_FOR_CUPS = 6
    EXITING = 7

class NotEnoughResources(Exception):
    """Exception if machine not have resources"""
    def __init__(self, coffee, resource, need, have):
        self.coffee = coffee
        self.resource = resource
        self.need = need
        self.have = have
        super().__init__(f"""I don't have {self.resource} for {self.coffee}.
I have {self.have}, need {self.need}""")

    def __str__(self):
        return f"""I don't have {self.resource} for {self.coffee}.
I have {self.have}, need {self.need}"""

class Machine:
    """Coffeemachine class"""
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.action = MachineState.WAITING_FOR_ACTION
        self.coffee_types = [
            Coffee(water = 250, milk = 0, beans = 16, cost = 4, name = "Espresso"),
            Coffee(water = 350, milk = 75, beans = 20, cost = 7, name = "Latte"),
            Coffee(water = 200, milk = 100, beans = 12, cost = 6, name = "Capuccino")
            ]

    def print_interface(self):
        """Printing"""
        if self.action == MachineState.WAITING_FOR_ACTION:
            print("Write action(buy, fill, take, remaining, exit)")
        elif self.action == MachineState.COFFEE_SELECTING:
            print("What do you want to buy?")
            print("1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
        elif self.action == MachineState.WAITING_FOR_WATER:
            print("Enter the amount of water(maximum = 50000):")
        elif self.action == MachineState.WAITING_FOR_MILK:
            print("Enter the amount of milk(maximum = 10000)")
        elif self.action == MachineState.WAITING_FOR_BEANS:
            print("Enter the amount of beans(maximum = 10000)")
        elif self.action == MachineState.WAITING_FOR_CUPS:
            print("Enter the amount of cups(maximum = 1000)")

    def making_coffee(self, coffee: Coffee):
        """Espresso"""
        self.action = MachineState.MAKING_COFFEE
        try:
            print("Checking resources...")
            if self.water < coffee.water:
                raise NotEnoughResources(coffee.name, "water", coffee.water, self.water)
            if self.milk < coffee.milk:
                raise NotEnoughResources(coffee.name, "milk", coffee.milk, self.milk)
            if self.beans < coffee.beans:
                raise NotEnoughResources(coffee.name, "beans", coffee.beans, self.beans)
            if self.cups < 1:
                raise NotEnoughResources(coffee.name, "cups", 1, self.cups)
            print("I have enough resources for Espresso")
            self.water -= coffee.water
            self.beans -= coffee.beans
            self.milk -= coffee.milk
            self.money += coffee.cost
            self.cups -= 1
            print("Done!")
            print(f"Your {coffee.name}!")
        except NotEnoughResources as message:
            print(message)
        self.action = MachineState.WAITING_FOR_ACTION

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
        if self.action == MachineState.WAITING_FOR_WATER:
            try:
                user_input = int(user_input)
                if user_input < 1 or (user_input+self.water) > 50000:
                    raise ValueError
                self.water += user_input
                self.action = MachineState.WAITING_FOR_MILK
            except ValueError:
                print("Incorrect input")
        elif self.action == MachineState.WAITING_FOR_MILK:
            try:
                user_input = int(user_input)
                if user_input < 1 or (user_input+self.milk) > 10000:
                    raise ValueError
                self.milk += user_input
                self.action = MachineState.WAITING_FOR_BEANS
            except ValueError:
                print("Incorrect input")
        elif self.action == MachineState.WAITING_FOR_BEANS:
            try:
                user_input = int(user_input)
                if user_input < 1 or (user_input+self.beans) > 10000:
                    raise ValueError
                self.beans += user_input
                self.action = MachineState.WAITING_FOR_CUPS
            except ValueError:
                print("Incorrect input")
        elif self.action == MachineState.WAITING_FOR_CUPS:
            try:
                user_input = int(user_input)
                if user_input < 1 or (user_input+self.cups) > 1000:
                    raise ValueError
                self.cups += user_input
                self.action = MachineState.WAITING_FOR_ACTION
            except ValueError:
                print("Incorrect input")

    def input_method(self, user_input):
        """Input"""
        if user_input == "buy" and self.action == MachineState.WAITING_FOR_ACTION:
            self.action = MachineState.COFFEE_SELECTING
        elif user_input == "back":
            self.action = MachineState.WAITING_FOR_ACTION
        elif user_input in ("1", "2", "3") and self.action == MachineState.COFFEE_SELECTING:
            self.making_coffee(self.coffee_types[int(user_input)-1])
        elif user_input == "fill" and self.action == MachineState.WAITING_FOR_ACTION:
            self.action = MachineState.WAITING_FOR_WATER
        elif self.action in (MachineState.WAITING_FOR_MILK, MachineState.WAITING_FOR_WATER,
           MachineState.WAITING_FOR_BEANS, MachineState.WAITING_FOR_CUPS):
            self.fill(user_input)
        elif user_input == "take" and self.action == MachineState.WAITING_FOR_ACTION:
            self.take()
        elif user_input == "remaining" and self.action == MachineState.WAITING_FOR_ACTION:
            self.remaining()
        elif user_input == "exit" and self.action == MachineState.WAITING_FOR_ACTION:
            self.action = MachineState.EXITING
        else:
            print("Unknown command")
