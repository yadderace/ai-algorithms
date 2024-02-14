import random

from enum import Enum

# class MoveDirection(Enum):
#     UP_LEFT = 1
#     UP = 2
#     UP_RIGHT = 3
#     LEFT = 4
#     RIGHT = 5
#     LEFT_DOWN = 6
#     DOWN = 7
#     RIGHT_DOWN = 8

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

    def move_queen(self, queen_number, direction, steps = 1):
        if (queen_number < 1) or (queen_number > len(self.queens_positions)) and (self.is_valid_move(queen_number, direction, steps)):
            return False

        row, col = self.queens_positions[queen_number - 1]
        row, col = self.get_new_positions(row, col, direction, steps)

        # if direction == 1 and row > 0 and col > 0:
        #     row -= steps
        #     col -= steps
        # elif direction == 2 and row > 0:
        #     row -= steps
        # elif direction == 3 and row > 0 and col < self.n_dim - 1:
        #     row -= steps
        #     col += steps
        # elif direction == 4 and col > 0:
        #     col -= steps
        # elif direction == 5 and col < self.n_dim - 1:
        #     col += steps
        # elif direction == 6 and row < self.n_dim - 1 and col > 0:
        #     row += steps
        #     col -= steps
        # elif direction == 7 and row < self.n_dim - 1:
        #     row += steps
        # elif direction == 8 and row < self.n_dim - 1 and col < self.n_dim - 1:
        #     row += steps
        #     col += steps
        # else:
        #     return False

        if self.board[row][col] == 0:
            self.board[self.queens_positions[queen_number - 1][0]][self.queens_positions[queen_number - 1][1]] = 0
            self.board[row][col] = 1
            self.queens_positions[queen_number - 1] = (row, col)
            return True
        else:
            return False

    def move_queen_without_action(self, queen_number, direction, steps = 1):
        if queen_number < 1 or queen_number > len(self.queens_positions):
            return None

        row, col = self.queens_positions[queen_number - 1]
        row, col = self.get_new_positions(row, col, direction, steps)
        # if direction == 1 and row > 0 and col > 0:
        #     row -= steps
        #     col -= steps
        # elif direction == 2 and row > 0:
        #     row -= steps
        # elif direction == 3 and row > 0 and col < self.n_dim - 1:
        #     row -= steps
        #     col += steps
        # elif direction == 4 and col > 0:
        #     col -= steps
        # elif direction == 5 and col < self.n_dim - 1:
        #     col += steps
        # elif direction == 6 and row < self.n_dim - 1 and col > 0:
        #     row += steps
        #     col -= steps
        # elif direction == 7 and row < self.n_dim - 1:
        #     row += steps
        # elif direction == 8 and row < self.n_dim - 1 and col < self.n_dim - 1:
        #     row += steps
        #     col += steps
        # else:
        #     return None

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

    def get_queen_next_moves(self, queen_number, max_spaces = None):
        next_moves = []

        for direction in range(1, 9):

            for steps in range(1, min(self.n_dim, max_spaces)):
                if(self.is_valid_move(queen_number, direction, steps)):
                    next_identifier = self.move_queen_without_action(queen_number, direction, steps)
                    if next_identifier:
                        next_moves.append({'identifier': next_identifier, 'queen': queen_number, 'direction': direction, 'steps': steps})

        return next_moves
    
    def cost_queens(self, identifier):
        cost = 0

        board, queens_positions = self._construct_board_from_identifier(identifier)
        
        for i in range(self.n_queens):
            row, col = queens_positions[i]
            # Count queens in the same row
            cost += sum(1 for c in range(self.n_dim) if board[row][c] != 0)
            # Count queens in the same column
            cost += sum(1 for r in range(self.n_dim) if board[r][col] != 0)
            # Subtract 2 to account for counting the current queen twice
            cost -= 2  

            # Check diagonals formed by the current queen
            for j in range(i + 1, self.n_queens):
                row_j, col_j = queens_positions[j]
                if abs(row - row_j) == abs(col - col_j):
                    cost += 2
        return cost // 2

    def _construct_board_from_identifier(self, identifier):
        board = [[0] * self.n_dim for _ in range(self.n_dim)]
        queens_positions = []
        # Parse the identifier string to get the positions of queens
        index = 0
        for row in range(self.n_dim):
            for col in range(self.n_dim):
                if identifier[index] == '1':
                    board[row][col] = 1
                    queens_positions.append((row, col))
                index += 1
        return board, queens_positions

    def get_identifier(self, board=None):
        if board is None:
            board = self.board

        identifier = ""
        for row in board:
            for value in row:
                identifier += str(value)
        return identifier
    
    def get_new_positions(self, row, col, direction, steps):
        
        new_col = col
        new_row = row

        if direction == 1 and row >= steps and col >= steps:
            new_row, new_col = row - steps, col - steps
        elif direction == 2 and row >= steps:
            new_row -= steps
        elif direction == 3 and row >= steps and col + steps < self.n_dim:
            new_row -= steps
            new_col += steps
        elif direction == 4 and col >= steps:
            new_col -= steps
        elif direction == 5 and col + steps < self.n_dim:
            new_col += steps
        elif direction == 6 and row + steps < self.n_dim and col >= steps:
            new_row += steps
            new_col -= steps
        elif direction == 7 and row + steps < self.n_dim:
            new_row += steps
        elif direction == 8 and row + steps < self.n_dim and col + steps < self.n_dim:
            new_row += steps
            new_col += steps
        else:
            return None, None
        
        return new_row, new_col
    
    def is_valid_move(self, queen_number, direction,  steps):
        row, col = self.queens_positions[queen_number - 1]
        
        # Determine the new position after the move
        new_row, new_col = self.get_new_positions(row, col, direction, steps)
        
        # Veriying if there's a new position for the queen
        if(new_row == None or new_col == None):
            return False
        
        # Check if the new position is within the board boundaries and not occupied by another queen
        if not (0 <= new_row < self.n_dim and 0 <= new_col < self.n_dim and self.board[new_row][new_col] == 0):
            return False
        
        # Check if there are any queens in the path of the moving queen
        for i, (q_row, q_col) in enumerate(self.queens_positions):
            
            # Just check if it's a different queen
            if i != (queen_number - 1):
                
                # Check if the current queen is in the path of the moving queen
                if (direction == 1) and (q_row < row) and (q_col < col) and (row - q_row == col - q_col):
                    if (q_row >= new_row) and (q_col >= new_col):
                        return False
                elif (direction == 2) and (q_row < row) and (q_col == col):
                    if (q_row >= new_row):
                        return False
                elif (direction == 3) and (q_row < row) and (q_col > col) and (row - q_row == q_col - col):
                    if (q_row >= new_row) and (q_col <= new_col):
                        return False
                elif (direction == 4) and (q_row == row) and (q_col < col):
                    if (q_col >= new_col):
                        return False
                elif (direction == 5) and (q_row == row) and (q_col > col):
                    if q_col <= new_col:
                        return False
                elif (direction == 6) and (q_row > row) and (q_col < col) and (q_row - row == col - q_col):
                    if q_row <= new_row and q_col >= new_col:
                        return False
                elif (direction == 7) and (q_row > row and q_col == col):
                    if q_row <= new_row:
                        return False
                elif (direction == 8) and (q_row > row) and (q_col > col) and (q_row - row == q_col - col):
                    if (q_row <= new_row) and (q_col <= new_col):
                        return False
        
        return True
        