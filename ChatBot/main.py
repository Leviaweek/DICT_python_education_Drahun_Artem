import chatbot
def main():
    """Main func"""
    try:
        bot = chatbot.ChatBot("DICT_Bot", 2022)
        print(bot)
        bot.bot_greeting_user()
        bot.remainding()
        bot.counting()
        bot.tests()
        bot.goodbye()
    except KeyboardInterrupt:
        print("Goodbye, have a nice day")

if __name__ == "__main__":
    main()