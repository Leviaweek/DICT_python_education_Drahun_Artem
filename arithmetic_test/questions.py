"""All level of tests"""
from test import Test

class Easy(Test):
    """Class for easy level test"""
    def __init__(self):
        self.operations = ["+", "-"]
        self.rand_min = 1
        self.rand_max = 10
        self.name = "easy"
        self.tests_number = 10

class Medium(Test):
    """Class for meidum level test"""
    def __init__(self):
        self.operations = ["+", "-", "*", "/"]
        self.rand_min = -100
        self.rand_max = 100
        self.name = "normal"
        self.tests_number = 15

class Hard(Test):
    """Class for hard level test"""
    def __init__(self):
        self.operations = ["+", "-", "*", "/"]
        self.rand_min = -1000
        self.rand_max = 1000
        self.name = "hard"
        self.tests_number = 20

class Unreal(Test):
    """Class for unreal level test"""
    def __init__(self):
        self.operations = ["**"]
        self.rand_min = 2
        self.rand_max = 10
        self.name = "unreal"
        self.tests_number = 25
