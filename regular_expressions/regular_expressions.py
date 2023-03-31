"""Regular expressions class module"""
import re

class RegularExpressions:
    """ReqexParser class"""

    def __init__(self) -> None:
        self.expression = ""
        self.string = ""

    def __take_result(self) -> bool:
        """Take string"""
        return re.match(self.expression, self.string) is not None

    def loop(self) -> None:
        """Regex loop"""
        while True:
            user_input = input("Input in format \"expression|string: ")
            try:
                self.expression, self.string = user_input.split(sep="|")
            except ValueError:
                print("You read what i write for you? READ TEXT!!!")
                continue
            print(self.__take_result())
 