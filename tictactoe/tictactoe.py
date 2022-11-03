"""game TicTacToe"""
import random
EMPTY = ' '
PLAYER1 = 'x'
PLAYER2 = 'o'

class TicTacToe:
    """TicTacToe class"""

    def __init__(self):
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.who_move = random.choice((PLAYER1,PLAYER2))
        self.winner = EMPTY

    def print_board(self):
        """Print Board"""

        print("_______")
        for i in self.board:
            for j in i:
                print(f"|{j}", end="")
            print("|")
        print("_______")

    def check_diagonals(self):
        """Checking diagonals for winner"""

        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY
            or self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY):
            self.winner = self.who_move

    def check_horizontal_lines(self):
        """Check horizontal lines for winner"""
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != EMPTY:
                self.winner = self.who_move
                break

    def check_vertical_lines(self):
        """Check vertical lines for winner"""
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != EMPTY:
                self.winner = self.who_move
                break

    def check_draw(self):
        """Check draw"""
        if not any(EMPTY in i for i in self.board):
            self.winner = None

    def game_move(self, coord_x: int, coord_y: int):
        """Game move results"""

        if self.board[coord_x][coord_y] == EMPTY:
            self.board[coord_x][coord_y] = self.who_move
        else:
            print("Cell is used")

def gameplay():
    """GamePlay"""

    game = TicTacToe()
    while True:
        game.print_board()
        while True:
            user_input = input(f"Write coordinates for {game.who_move}: ")
            split_use = user_input.split()
            if len(split_use) == 2 and split_use[0].isdigit() and split_use[1].isdigit():
                coord_x, coord_y = map(int, split_use)
                if 1 <= coord_x <= 3 and 1 <= coord_y <= 3:
                    game.game_move(coord_x-1, coord_y-1)
                    break
            print("Not correct coordinates")
        game.check_diagonals()
        game.check_horizontal_lines()
        game.check_vertical_lines()
        if game.winner in (PLAYER1, PLAYER2):
            game.print_board()
            print(f"Player {game.who_move} win!")
            break
        game.check_draw()
        if game.winner is None:
            print("Oops, you have draw!")
            break
        if game.who_move == PLAYER1:
            game.who_move = PLAYER2
        elif game.who_move == PLAYER2:
            game.who_move = PLAYER1

def main():
    """Main start point"""
    print("Hello, it's TicTacToe game")
    print("I think you know how to play")
    while True:
        print("Do you want play?(print yes or no)")
        user_input = input("> ")
        if user_input.lower() == "yes":
            gameplay()
        elif user_input.lower() == "no":
            break
        else:
            print("I don't now what you say...")

if __name__ == "__main__":
    main()
