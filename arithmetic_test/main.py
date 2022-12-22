"""Arithmetic test main file"""
import questions

def testing():
    """Testing menu"""
    while True:
        print("""Choose level:
1. Easy (simple operations with numbers 2-9)
2. Normal (simple operations with numbers -100 - 100
3. Hard (mixed operations with numbers -1000 - 1000)
4. Unreal(squares of numbers from 10 to 1000)
0. Exit
(If the operation is division, then use rounding up to two numbers after the point
for float numbers use dot)""")
        user_input = input(">>> ").strip()
        match user_input:
            case "1":
                test = questions.Easy()
            case "2":
                test = questions.Medium()
            case "3":
                test = questions.Hard()
            case "4":
                test = questions.Unreal()
            case "0":
                return
            case _:
                print("Unknown input")
                continue
        test.test_menu()

def main():
    """Tests start point"""
    try:
        testing()
    except KeyboardInterrupt:
        print("Exiting...")
    print("Goodbye")

if __name__ == "__main__":
    main()
