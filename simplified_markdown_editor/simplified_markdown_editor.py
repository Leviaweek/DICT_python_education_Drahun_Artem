"""markdown editor"""

class MarkdownEditor:
    """Markdown main class"""

    def __init__(self):
        self.text = ""

    def __str__(self):
        """Return text"""
        return self.text

    def add_plain(self, text):
        """adding plain"""
        self.text += text

    def add_bold(self, text):
        """adding bold"""
        self.text += f"**{text}**"

    def add_italic(self, text):
        """adding italic"""
        self.text += f"*{text}*"

    def add_header(self, number, string):
        """adding header"""
        self.text += f"{'#' * number} {string}\n"

    def add_link(self, title, url):
        """adding link"""
        self.text += f"[{title}]({url})"

    def add_code(self, text):
        """Adding inline-code"""
        self.text += f"'{text}'"

    def add_ordered_list(self, number):
        """adding ordered list"""
        for i in range(1, number+1):
            self.text += f"{i}. {self.input_string(f'Row #{i}')}\n"

    def add_unordered_list(self, number):
        """adding unordered list"""
        for i in range(1, number+1):
            self.text += f"* {self.input_string(f'Row #{i}')}\n"

    def add_newline(self):
        """creating newline"""
        self.text += "\n"

    def number_input(self, text):
        """Inputing number"""
        while True:
            user_input = input(f"{text}:> ")
            try:
                return int(user_input)
            except ValueError:
                print("this isn't integer")

    def input_string(self, text):
        """Inputing text"""
        while True:
            user_input = input(f"{text}:> ")
            if user_input:
                return user_input
            print("String cannot be empty")

    def header_input_check(self):
        """Checking header level"""
        while True:
            number = self.number_input("Level")
            if 1 <= number <= 6:
                return number
            print("Header have levels from 1 to 6")

    def markdown_menu(self):
        """Markdown main menu"""
        while True:
            print("""Special commands: !help !done""")
            user_input = input(">>> ")
            match user_input.lower():
                case "!help":
                    self.help_print()
                    print(self)
                    continue
                case "plain":
                    self.add_plain(self.input_string("Text"))
                case "bold":
                    self.add_bold(self.input_string("Text"))
                case "italic":
                    self.add_italic(self.input_string("Text"))
                case "header":
                    self.add_header(self.header_input_check(), self.input_string("Text"))
                case "link":
                    self.add_link(self.input_string("Title"), self.input_string("URL"))
                case "inline-code":
                    self.add_code(self.input_string("Text"))
                case "ordered-list":
                    self.add_ordered_list(self.number_input("Number of rows"))
                case "unordered-list":
                    self.add_unordered_list(self.number_input("Number of rows"))
                case "new line":
                    self.add_newline()
                case "!done":
                    filename = "output.md"
                    self.file_save(filename)
                    continue
                case _:
                    print("Unknown command")
            print(self)

    def help_print(self):
        """help printer"""
        print("""Available formatters:
plain bold italic header link inline-code ordered-list unordered-list new-line""")

    def file_save(self, filename):
        """Saving text in the file"""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.text)

def main():
    "markdown editor start point"
    print("Hello, it's simplified markdown editor")
    while True:
        print("Do you want start?(yes or no)")
        user_input = input(">>> ")
        if user_input.lower() == "yes":
            editor = MarkdownEditor()
            editor.markdown_menu()
        elif user_input.lower() == "no":
            print("Goodbye")
            return
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
