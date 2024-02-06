import random

class ChessBoard:
    def __init__(self, n_dim, n_queens):
        if n_dim < n_queens:
            raise ValueError("n_dim must be greater than or equal to n_queens")

        self.n_dim = n_dim
        self.n_queens = n_queens
        self.board = [[0] * n_dim for _ in range(n_dim)]
        self.queens_positions = []

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join(map(str, row)) + "\n"
        return board_str

    def place_queens(self, queens_positions=None):
        if queens_positions is None:
            queens_positions = self._generate_random_queens()

        if len(queens_positions) != self.n_queens:
            raise ValueError("Number of queen positions must be equal to n_queens")

        for i, (row, col) in enumerate(queens_positions, start=1):
            if row < 0 or row >= self.n_dim or col < 0 or col >= self.n_dim:
                raise ValueError("Queen position out of bounds")

            self.board[row][col] = i

        self.queens_positions = queens_positions

    def _generate_random_queens(self):
        queens_positions = []
        for _ in range(self.n_queens):
            row = random.randint(0, self.n_dim - 1)
            col = random.randint(0, self.n_dim - 1)
            queens_positions.append((row, col))
        return queens_positions

    def move_queen(self, queen_number, direction):
        if queen_number < 1 or queen_number > len(self.queens_positions):
            return False

        row, col = self.queens_positions[queen_number - 1]

        if direction == 1 and row > 0 and col > 0:
            row -= 1
            col -= 1
        elif direction == 2 and row > 0:
            row -= 1
        elif direction == 3 and row > 0 and col < self.n_dim - 1:
            row -= 1
            col += 1
        elif direction == 4 and col > 0:
            col -= 1
        elif direction == 5 and col < self.n_dim - 1:
            col += 1
        elif direction == 6 and row < self.n_dim - 1 and col > 0:
            row += 1
            col -= 1
        elif direction == 7 and row < self.n_dim - 1:
            row += 1
        elif direction == 8 and row < self.n_dim - 1 and col < self.n_dim - 1:
            row += 1
            col += 1
        else:
            return False

        if self.board[row][col] == 0:
            self.board[self.queens_positions[queen_number - 1][0]][self.queens_positions[queen_number - 1][1]] = 0
            self.board[row][col] = queen_number
            self.queens_positions[queen_number - 1] = (row, col)
            return True
        else:
            return False

    def move_queen_without_action(self, queen_number, direction):
        if queen_number < 1 or queen_number > len(self.queens_positions):
            return None

        row, col = self.queens_positions[queen_number - 1]

        if direction == 1 and row > 0 and col > 0:
            row -= 1
            col -= 1
        elif direction == 2 and row > 0:
            row -= 1
        elif direction == 3 and row > 0 and col < self.n_dim - 1:
            row -= 1
            col += 1
        elif direction == 4 and col > 0:
            col -= 1
        elif direction == 5 and col < self.n_dim - 1:
            col += 1
        elif direction == 6 and row < self.n_dim - 1 and col > 0:
            row += 1
            col -= 1
        elif direction == 7 and row < self.n_dim - 1:
            row += 1
        elif direction == 8 and row < self.n_dim - 1 and col < self.n_dim - 1:
            row += 1
            col += 1
        else:
            return None

        if self.board[row][col] == 0:
            new_queens_positions = self.queens_positions[:]
            new_queens_positions[queen_number - 1] = (row, col)

            new_board = [[0] * self.n_dim for _ in range(self.n_dim)]
            for i, (row, col) in enumerate(new_queens_positions, start=1):
                new_board[row][col] = i

            return self.get_identifier(new_board)
        else:
            return None

    def print_board_from_identifier(self, identifier):
        n = self.n_dim
        board = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                board[i][j] = int(identifier[i * n + j])

        print("Board:")
        for row in board:
            print(" ".join(map(str, row)))

    def get_identifier(self, board=None):
        if board is None:
            board = self.board

        identifier = ""
        for row in board:
            for value in row:
                identifier += str(value)
        return identifier
    
# Example usage:
n_dim = 8
n_queens = 5
chess_board = ChessBoard(n_dim, n_queens)
chess_board.place_queens()
print(chess_board)

# Move the first queen up
print(chess_board.move_queen(4, 2))
print(chess_board)

print(chess_board.get_identifier())

id = chess_board.move_queen_without_action(3,6)
if id != None:
    chess_board.print_board_from_identifier(id)
print("")
print(chess_board)