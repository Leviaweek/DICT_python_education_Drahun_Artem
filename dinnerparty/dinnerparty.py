"""Dinnerparty with friends"""

import sys
import random

def main() -> None:
    """Main start point"""
    print("\t\tDinnertParty with you friends")
    print("\t\tNOT A PENNY MORE\n\n")
    print("\tYou can write number of you friends and sum.")
    print("\tI will divide the amount by the number of friends")
    print("\tOne lucky person can will be lucky)")
    print("\tIf you have friends with the same name")
    print("\tThen write numbers next to the names, this is in your interest\n\n")
    dinnerparty()


def dinnerparty() -> None:
    """DinnerParty start point"""
    input_symbol = "> "
    print("Enter the number of friends joining (including you):")
    friends = {}
    friends_number = input(input_symbol)
    while not friends_number.isnumeric():
        print("Please, try again")
        friends_number = input(input_symbol)
    friends_number = int(friends_number)
    if friends_number <= 0:
        print("Oh, you're pretty lonely :(")
        sys.exit(0)
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {f"{input(input_symbol)}": 0 for key in range(friends_number)}
    print("Enter the total amount:")
    amount = input(input_symbol)
    while not amount.isnumeric() and amount != "":
        print("Please, try again")
        amount = input(input_symbol)
    amount = float(amount)
    while amount < 0:
        print("Please, try again")
        amount = input(input_symbol)
    amount = float(amount)
    print("Who is lucky?")
    lucky = input(input_symbol)
    while not (lucky.lower() == "yes" or lucky.lower() == "no"):
        print("Please, try again")
        lucky = input(input_symbol)
    if lucky == "yes":
        lucky_friend = random.choice(list(friends))
        print(f"{lucky_friend} is lucky friend!")
        for key in friends:
            if key == lucky_friend:
                continue
            friends[f"{key}"] = round(amount/(friends_number - 1), 2)
    else:
        for key in friends:
            friends[f"{key}"] = round(amount/friends_number, 2)
    print(friends)

if __name__ == "__main__":
    main()
