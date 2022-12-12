"""Console Chatbot"""

class ChatBot:
    """Chatbot main class"""
    def __init__(self, bot_name, year_creating):
        self.bot_name = bot_name
        self.year_creating = year_creating

    def __str__(self):
        """Bot greeting print"""
        return f"""Hello! My name is {self.bot_name}.
I was created in {self.year_creating}."""

    def bot_greeting_user(self):
        """Bot ask username"""
        print("Please, remind me your name:")
        user_name = input(">>> ")
        print(f"What a great name you have, {user_name}!")

    def int_input(self):
        """For all user inputs"""
        while True:
            try:
                user_input = int(input(">>> "))
                if user_input < 0:
                    raise ValueError
                return user_input
            except ValueError:
                print("Please, input only positive numbers")

    def remainding(self):
        """bot remind user age"""
        print("Let me guess your age.")
        print("Enter remainders of dividing your age by 3, 5 and 7.")
        remainder3 = self.int_input()
        remainder5 = self.int_input()
        remainder7 = self.int_input()
        age = self.age_calulating(remainder3, remainder5, remainder7)
        print(f"Your age is {age}; that's good time for programming")

    def age_calulating(self, remainder3, remainder5, remainder7):
        """bot calculate user age"""
        age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
        return age

    def counting(self):
        """Bot count from 0 to user number"""
        print("Now I will prove to you that I can count to any number you want.")
        user_number = self.int_input()
        for i in range(user_number):
            print(f"{i} !")

    def test_creating(self, question, answer):
        """Creater tests"""
        while True:
            print(question)
            user_answer = self.int_input()
            if user_answer == answer:
                print("Nice!")
                break
            print("Incorrect")


    def tests(self):
        """Bot asks the player questions"""
        print("Let's test your programming knowledge.")
        self.test_creating("""What is the language of programming?
1. C#
2. C++
3. Python
4. Assembler""", 3)
        self.test_creating("""Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""", 2)
        print("Completed, have a nice day!")

    def goodbye(self):
        """Boy say goodbye for user"""
        print("Congratulations, have a nice day!")