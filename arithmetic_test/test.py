"""Test main class file"""
import random
import math
from abc import ABC
from question import Question

class Test(ABC):
    """Main class for all tests"""

    def __init__(self):
        self.operations = None
        self.rand_min = None
        self.rand_max = None
        self.name = None
        self.tests_number = None

    def test_creator(self) -> Question:
        """Universal method for creating questions"""
        first_number = random.randint(self.rand_min, self.rand_max)
        operation = random.choice(self.operations)
        second_number = random.randint(self.rand_min, self.rand_max)
        match(operation):
            case "+":
                answer = first_number + second_number
            case "-":
                answer = first_number - second_number
            case "*":
                answer = first_number * second_number
            case "/":
                answer = first_number / second_number
                if answer % 1 == 0:
                    answer = int(answer)
                else:
                    answer = round(answer, 2)
            case "**":
                answer = math.pow(first_number, second_number)
        return Question(f"{first_number} {operation} {second_number}", float(answer))

    def test_menu(self) -> None:
        """Main tests menu"""
        result = 0
        for _ in range(self.tests_number):
            question = self.test_creator()
            print(question)
            while True:
                try:
                    answer = float(input(">>> ").strip())
                    break
                except ValueError:
                    print("Incorrect input")
            if question.check_answer(answer):
                print("Done!")
                result += 1
            else:
                print("Wrong!")
        print(f"You have {result} from {self.tests_number} true answers")
        while True:
            print("Do you want save result?(y/n)")
            user_input = input(">>> ").lower()
            if user_input == "y":
                print("Enter your name")
                name = input(">>> ")
                self.file_save(name, result)
                break
            if user_input == "n":
                break
            print("Incorrect")
        print("Goodbye!")

    def file_save(self, name: str, result: str) -> None:
        """saving game result"""
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"{name} have {result} correct answers from 10 in {self.name} level\n")
