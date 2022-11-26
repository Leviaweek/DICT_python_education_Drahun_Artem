"""Arithmetic test"""
import random

class Test:
    """Main class for tests"""

    def __init__(self):
        self.random_operation = ("+", "-", "*", "/")

    def test_for_user(self, minimal, maximal, operation = ""):
        """main test for all tests"""
        true_answers = 0
        for _ in range(25):
            first_number = random.randint(minimal, maximal)
            if operation != "**":
                operation = random.choice(self.random_operation)
                second_number = random.randint(minimal, maximal)
            first_number = random.randint(minimal, maximal)
            second_number = random.randint(2, 10)
            print(first_number, operation, second_number)
            true_answers += self.user_answer(first_number, second_number, operation)
        result = f"{true_answers}/25 correct answers"
        print("Do you want save your result?(yes or no)")
        while True:
            user_input = input(">>> ")
            if user_input.lower() == "yes":
                print("Print your name")
                name = input(">>> ")
                self.save_file(name, result)
                break
            elif user_input.lower() == "no":
                return
            else:
                print("Unknown input")

    def user_answer(self, first_number, second_number, operation):
        """check user answer"""
        match operation:
            case "+":
                result = first_number + second_number
            case "-":
                result = first_number - second_number
            case "*":
                result = first_number * second_number
            case "/":
                result = round(float(first_number) / float(second_number), 2)
            case "**":
                result = first_number ** second_number
        while True:
            user_input = input(">>> ")
            try:
                if operation != "/":
                    user_input = int(user_input)
                else:
                    user_input = float(user_input)
                if user_input == result:
                    print("Right!")
                    return 1
                print("Wrong")
                return 0
            except ValueError:
                print("Write only numbers")

    def save_file(self, name, result):
        """saving game result"""
        with open("results.txt", "w", encoding="utf-8") as file:
            file.write(f"{name} have {result} correct answers")

    def test_menu(self):
        """main menu of test"""
        while True:
            print("""Choose level:
1. Easy (simple operations with numbers 2-9)
2. Normal (simple operations with numbers 10-40
3. Hard (mixed operations with numbers 1-1000)
4. Unreal(squares of numbers from 10 to 1000)
0. Exit
(If the operation is division, then use rounding up to two numbers after the point
for float numbers use dot)""")
            user_input = input(">>> ")
            match user_input:
                case "1":
                    self.test_for_user(2, 9)
                case "2":
                    self.test_for_user(10, 40)
                case "3":
                    self.test_for_user(1, 10000)
                case "4":
                    self.test_for_user(10, 1000, "**")
                case "0":
                    return
                case _:
                    print("Unknown input")

def main():
    """test start point"""
    print("It's my arithmetic test")
    print("Do you wanna start?(yes or no)")
    while True:
        user_input = input(">>> ")
        if user_input.lower() == "yes":
            arithmetic_test = Test()
            arithmetic_test.test_menu()
        elif user_input.lower() == "no":
            break
        else:
            print("Unknown command")
    print("Goodbye")

if __name__ == "__main__":
    main()
