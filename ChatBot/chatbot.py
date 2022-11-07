"""Console Chatbot"""

print("""Hello! My name is DICT_Bot.
I was created in 2022.""")
user_name = input("Please, remind me your name:\n> ")
print(f"What a great name you have, {user_name}!")
print("""Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")
remainder3 = input("> ")
remainder5 = input("> ")
remainder7 = input("> ")
while (not remainder3.isnumeric()
        or not remainder5.isnumeric()
        or not remainder7.isnumeric()):
    print("Please, write only numbers")
    remainder3 = input("> ")
    remainder5 = input("> ")
    remainder7 = input("> ")
age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
print(f"Your age is {age}; that's good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
user_number = input("> ")
while not user_number.isnumeric():
    print("Plase, write only numbers")
    user_number = input("> ")
for value in range(int(user_number)+1):
    print(f"{value} !")
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("""How can I find out the id of string?
1. isinstance()
2. type()
3. id()
4. isnumeric()""")
user_response1 = input("> ")
while user_response1 != "3" or not user_response1.isnumeric():
    print("Please, try again")
    user_response1 = input("> ")
print("""what type of data is the number 0.1?
1. String
2. Integer
3. Bool
4. Float""")
user_response2 = input("> ")
while user_response2 != "4" or not user_response2.isnumeric():
    print("Please, try again")
    user_response2 = input("> ")
print("All answers are correct!")
print("Congratulations, have a nice day!")
