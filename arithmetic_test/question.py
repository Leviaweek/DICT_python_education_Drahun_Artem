"""Test structure"""

class Question:
    """Question class"""
    def __init__(self, question, answer: int | float):
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

    def check_answer(self, answer: int | float) -> bool:
        """Check user answer and true answer"""
        return self.answer == answer
