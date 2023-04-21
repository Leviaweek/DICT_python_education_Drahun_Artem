"""Remote server imitation"""
import json
import random
from string import ascii_letters, digits

class Server:
    """Remote server class"""

    def __init__(self):
        self.__login = self.__generate_login()
        self.__password = self.__generate_password()

    def __generate_login(self) -> str:
        """Generate login"""
        with open("logins.txt", "r") as file:
            logins = file.read().splitlines()
        return random.choice(logins).strip()

    def __generate_password(self) -> str:
        """Generate password"""
        symbols = ascii_letters + digits
        password_len = random.randint(10, 30)
        return "".join([random.choice(symbols) for _ in range(password_len)])

    def __response(self, login, password) -> str:
        """Response to client
        :param login: client login
        :param password: client password
        :return: response to client
        """
        if login != self.__login:
            return json.dumps({"result": "Wrong login!"})
        if not self.__password.startswith(password) and self.__login == login:
            return json.dumps({"result": "Wrong password!"})
        if self.__password.startswith(password) and self.__password != password:
            return json.dumps({"result": "Exception happened during login"})
        if password == self.__password:
            return json.dumps({"result": "Connection success!"})
        return json.dumps({"result": "What are you doing....?"})

    def request(self, request) -> str:
        """Request to server"""
        request = json.loads(request)
        return self.__response(request["login"], request["password"])
