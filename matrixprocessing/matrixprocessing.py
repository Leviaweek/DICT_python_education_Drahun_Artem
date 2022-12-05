"""Matrix calculator"""

class Calculator:
    """Calculator class"""

    def print_matrix(self, matrix: list):
        """Printing matrix"""
        for i in matrix:
            for j in i:
                print(j, end=" ")
            print()

    def creating_matrix(self, width: int, height: int) -> list:
        """Creating matrix"""
        matrix = []
        print("Print matrix")
        for _ in range(width):
            while True:
                try:
                    user_input = list(map(int, input().split()))
                    if len(user_input) != height:
                        raise ValueError
                    matrix.append(user_input)
                    break
                except ValueError:
                    print("Incorrect input")
        self.print_matrix(matrix)
        return matrix

    def matrix_input(self) -> list:
        """Creating matrix size"""
        while True:
            try:
                width, height = map(int, input("Enter parameters of matrix: ").split())
                if width <= 0 or height <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Incorrect input")
        matrix = self.creating_matrix(width, height)
        return matrix

    def matrix_sum(self, matrix1, matrix2) -> None:
        """Matrix sum calculate"""
        matrix_sum = []
        if (len(matrix1) != len(matrix2)
            or len(matrix1[0]) != len(matrix2[0])):
            print("Matrix not have sum")
            return
        matrix1_height = len(matrix1)
        for i in range(matrix1_height):
            matrix_height = []
            for j in range(len(matrix1[0])):
                matrix_height.append(matrix1[i][j] + matrix2[i][j])
            matrix_sum.append(matrix_height)
        print("Your matrix sum:")
        self.print_matrix(matrix_sum)

    def constant_input(self) -> int:
        """Inputing constant"""
        while True:
            try:
                user_constant = int(input("Write a constant: "))
                return user_constant
            except ValueError:
                print("Incorrect input")

    def multiply_by_constant(self, matrix: list, constant: int) -> None:
        """Multiplying matrix by constant"""
        matrix_multiply = []
        matrix_height = len(matrix)
        for i in range(matrix_height):
            matrix_height = []
            for j in range(len(matrix[0])):
                matrix_height.append(matrix[i][j] * constant)
            matrix_multiply.append(matrix_height)
        print("Your matrix multiply:")
        self.print_matrix(matrix_multiply)

    def multiply_matrix(self, matrix1, matrix2):
        """Multiplying matrix"""
        if len(matrix1[0]) != len(matrix2):
            print("I can't multiply this matrix :(")
            return
        matrix1_height = len(matrix1)
        matrix2_height = len(matrix2)
        matrix_multiply = []
        for i in range(matrix1_height):
            matrix_height = []
            for j in range(matrix1_height):
                matrix_sum = 0
                for k in range(matrix2_height):
                    matrix_sum += matrix1[i][k] * matrix2[k][j]
                matrix_height.append(matrix_sum)
            matrix_multiply.append(matrix_height)
        self.print_matrix(matrix_multiply)

    def transp_main(self, matrix):
        """main transposition"""
        height = len(matrix)
        width = len(matrix[0])
        transp_matrix = []
        for i in range(width):
            transp_height = []
            for j in range(height):
                transp_height.append(matrix[j][i])
            transp_matrix.append(transp_height)
        self.print_matrix(transp_matrix)

    def transp_side(self, matrix):
        """transposition about the side diagonal"""
        height = len(matrix)
        width = len(matrix[0])
        transp_matrix = []
        for i in range(height):
            transp_height = []
            for j in range(width):
                transp_height.append(matrix[-j-1][-i-1])
            transp_matrix.append(transp_height)
        self.print_matrix(transp_matrix)

    def transp_vertical(self, matrix):
        """Vertical transposition"""
        height = len(matrix)
        width = len(matrix[0])
        transp_matrix = []
        for i in range(height):
            transp_height = []
            for j in range(width):
                transp_height.append(matrix[i][-j-1])
            transp_matrix.append(transp_height)
        self.print_matrix(transp_matrix)

    def transp_horizontal(self, matrix):
        """horizontal transposition"""
        height = len(matrix)
        width = len(matrix[0])
        transp_matrix = []
        for i in range(height):
            transp_height = []
            for j in range(width):
                transp_height.append(matrix[-i-1][j])
            transp_matrix.append(transp_height)
        self.print_matrix(transp_matrix)

    def determinant(self, matrix: list):
        """Matrix determinant"""
        if len(matrix) == len(matrix[0]) == 1:
            return matrix[0][0]
        height = len(matrix)
        determ = 0
        for i in range(height):
            minor_symbol = (-1) ** i
            determ += (self.determinant(self.minor(matrix, i, 0)) * minor_symbol * matrix[i][0])
        return determ

    def minor(self, matrix, i, j):
        """Matrix minors"""
        height = len(matrix)
        minor = []
        for horizontal in range(height):
            minor_height = []
            if horizontal == i:
                continue
            for vertical in range(height):
                if vertical == j:
                    continue
                minor_height.append(matrix[horizontal][vertical])
            minor.append(minor_height)
        return minor

    def inverse(self, matrix):
        """Inversion of matrix"""
        height = len(matrix)
        inversed_matrix = []
        for i in range(height):
            matrix_height = []
            for j in range(height):
                minor_symbol = (-1) ** (i+j)
                matrix_height.append(self.determinant(self.minor(matrix, i, j)) * minor_symbol)

            inversed_matrix.append(matrix_height)
        self.print_matrix(inversed_matrix)

    def matrix_transp_menu(self, matrix: list):
        """Menu transposition of matrix"""
        while True:
            print("""Choose one of the options:
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
            user_input = input(">>> ")
            match user_input:
                case "1":
                    self.transp_main(matrix)
                    break
                case "2":
                    self.transp_side(matrix)
                    break
                case "3":
                    self.transp_vertical(matrix)
                    break
                case "4":
                    self.transp_horizontal(matrix)
                    break
                case _:
                    print("Unknown command")

    def calculator_menu(self) -> None:
        """Calculator main menu"""
        while True:
            print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
            user_action = input()
            match user_action:
                case "1":
                    matrix1 = self.matrix_input()
                    matrix2 = self.matrix_input()
                    self.matrix_sum(matrix1, matrix2)
                case "2":
                    matrix = self.matrix_input()
                    constant = self.constant_input()
                    self.multiply_by_constant(matrix, constant)
                case "3":
                    matrix1 = self.matrix_input()
                    matrix2 = self.matrix_input()
                    self.multiply_matrix(matrix1, matrix2)
                case "4":
                    matrix = self.matrix_input()
                    self.matrix_transp_menu(matrix)
                case "5":
                    matrix = self.matrix_input()
                    if len(matrix) != len(matrix[0]):
                        print("Matrix isn't square!")
                        continue
                    determinant = self.determinant(matrix)
                    print(determinant)
                case "6":
                    matrix = self.matrix_input()
                    if len(matrix) != len(matrix[0]):
                        print("Matrix isn't square!")
                        continue
                    self.inverse(matrix)
                case "0":
                    return
                case _:
                    print("Unknown command")

def main():
    """Main function"""
    print("Hello, it's calculator for matrix")
    while True:
        print("Do you want start?(yes or no)")
        user_action = input().lower()
        if user_action == "yes":
            matrix_calculator = Calculator()
            matrix_calculator.calculator_menu()
        elif user_action == "no":
            break
        else:
            print("Unknown command")
    print("Goodbye")

if __name__ == "__main__":
    main()
