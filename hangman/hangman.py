"""Game Hangman"""

import random

WORDS = ["javascript", "python", "programming", "function"]

def main():
    """Main menu"""

    print("\t\t\tHANGMAN")
    print("To start write \"Start\", to exit write \"Exit\"")
    if input("> ").lower() == "start":
        hangman_game()
    else:
        print("Goodbye")


def hangman_game():
    """Game start point"""

    game_word = random.choice(WORDS) #Выбор случайного слова
    game_closed_word = list("-" * len(game_word)) #Закрытое слово
    used_letters = []
    mistakes = 0

    for letter in range(0,3):
        game_closed_word[letter] = game_word[letter] #Открытие первых трёх букв
    print("LET'S PLAY A GAME!!!")
    print("CAN YOU GUESS THE WORD?")
    print("IF NOT, THEN YOU WILL BE KILLED.")
    mistakes = checker(game_closed_word, game_word, mistakes, used_letters)
    if mistakes == 8:
        print("You made 8 mistakes and has been killed")
        print(f"Word is {game_word}")
    elif mistakes == 9:
        print("You don't guess")
        print(f"Word is {game_word}")
    elif mistakes < 8:
        print(f"You win, word is {game_word}")
    print("Want to try again?")
    print("If yes, write yes, if not, write something")
    if list(input("> ").lower()) == 'yes':
        main()
    else:
        print("Goodbye")

def checker(game_closed_word, game_word, mistakes, used_letters):
    """Word checker"""

    while "".join(game_closed_word) != game_word:
        used_letter_indicator = False #Обновляющийся индиктор для использованных букв
        print("Closed word: ", "".join(game_closed_word)) #Вывод массива в виде единого слова
        print("If you input all word, you have only one attempt")
        print("You can write used letter, which are open by the game")
        user_letter = input("input a letter or full word: > ")
        while (user_letter.isnumeric()
                or user_letter == ''
                or user_letter == ' '):
            user_letter = input("Please, try again: > ")
        user_letter = user_letter.lower()
        if len(user_letter) != 1:
            if user_letter != game_word:
                mistakes = 9
                break
            break
        for letter in used_letters: #Проверка наличия буквы в списке используемых букв
            if user_letter == letter.lower():
                print("You use this letter")
                used_letter_indicator = True
                break
        if used_letter_indicator is True:
            continue
        local_errors = 0
        for ind, letter in enumerate(game_closed_word):
            if user_letter == game_word[ind]:
                game_closed_word[ind] = user_letter
            else: local_errors += 1
        if local_errors == len(game_word):
            mistakes += 1
            print("You mistake")
            print(f"You have {mistakes} mistakes")
        used_letters.append(user_letter)
        if mistakes == 8:
            break
    return mistakes


if __name__ == "__main__":
    main()
