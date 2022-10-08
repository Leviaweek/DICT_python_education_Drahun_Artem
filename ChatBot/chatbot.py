"""Console Chatbot"""

print("""Hello! My name is DICT_Bot.
I was created in 2022.""")
name = input("Please, remind me your name:\n> ")
print(f"What a great name you have, {name}!")
print("""Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")
remainder3 = input("> ")
remainder5 = input("> ")
remainder7 = input("> ")
while (not remainder3.isnumeric()
        or not remainder5.isnumeric()
        or not remainder7.isnumeric()):
    print("Please, try again")
    remainder3 = input("> ")
    remainder5 = input("> ")
    remainder7 = input("> ")
age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
print(f"Your age is {age}; that's good time to start programming!")
