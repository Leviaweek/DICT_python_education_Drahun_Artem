"""Main file"""
from regular_expressions import RegularExpressions

def main():
    """Main function"""
    regex = RegularExpressions()
    try:
        regex.loop()
    except KeyboardInterrupt:
        print("\nYes, regex is shit!")
    print("Goodbye")

if __name__ == "__main__":
    main()
