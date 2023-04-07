"""main file"""
from web_parser import WebParser

def main():
    """main function"""
    url = "https://www.nature.com/nature/articles?sort=PubD0ate&year=2022&page=1"
    try:
        pages_number = int(input("Enter number of pages: "))
    except ValueError:
        print("Invalid number of pages")
        return
    pages_type = input("Enter type of pages: ").title()
    web_parser = WebParser(url, pages_number, pages_type)
    try:
        web_parser.parse()
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("Ok, goodbye!!!")
    print("Done!!!")

if __name__ == "__main__":
    main()