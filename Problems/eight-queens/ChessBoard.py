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

            self.board[row][col] = 1

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
            self.board[row][col] = 1
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
                new_board[row][col] = 1

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

    def get_queen_next_moves(self, queen_number):
        next_moves = []

        for direction in range(1, 9):
            next_identifier = self.move_queen_without_action(queen_number, direction)
            if next_identifier:
                next_moves.append({'identifier': next_identifier, 'queen': queen_number, 'direction': direction})

        return next_moves
    
    def cost_queens(self, identifier):
        cost = 0

        board = self._construct_board_from_identifier(identifier)
        
        for i in range(self.n_queens):
            row, col = self.queens_positions[i]

            # Count queens in the same row
            cost += sum(1 for c in range(self.n_dim) if board[row][c] != 0)
            # Count queens in the same column
            cost += sum(1 for r in range(self.n_dim) if board[r][col] != 0)
            # Subtract 2 to account for counting the current queen twice
            cost -= 2
            
            # Check diagonals formed by the current queen
            for j in range(i + 1, self.n_queens):
                row_j, col_j = self.queens_positions[j]
                if abs(row - row_j) == abs(col - col_j):
                    cost += 2

        # Each pair of queens is counted twice, so divide by 2
        return cost // 2

    def _construct_board_from_identifier(self, identifier):
        board = [[0] * self.n_dim for _ in range(self.n_dim)]
        # Parse the identifier string to get the positions of queens
        index = 0
        for row in range(self.n_dim):
            for col in range(self.n_dim):
                if identifier[index] == '1':
                    board[row][col] = 1
                index += 1
        return board

    def get_identifier(self, board=None):
        if board is None:
            board = self.board

        identifier = ""
        for row in board:
            for value in row:
                identifier += str(value)
        return identifier