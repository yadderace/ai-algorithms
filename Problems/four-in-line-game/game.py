import random

class FourInLine:
    DEFAULT_ROWS = 6
    DEFAULT_COLS = 7
    DEFAULT_PLAYER1_SYMBOL = 'X'
    DEFAULT_PLAYER2_SYMBOL = 'O'
    
    EMPTY_SPACE = ' '

    @property
    def game_board(self):
        """
        Get the current state of the game board.

        Returns:
            list: Matrix representing the current state of the game board.
        """
        return self.board

    @property
    def player1_symbol(self):
        return self.player1_symbol
    
    @property
    def player2_symbol(self):
        return self.player2_symbol
    
    def __init__(self, rows=DEFAULT_ROWS, cols=DEFAULT_COLS, player1_symbol=DEFAULT_PLAYER1_SYMBOL, player2_symbol=DEFAULT_PLAYER2_SYMBOL):
        """
        Initialize the Connect Four game.

        Args:
            rows (int): Number of rows in the game board (default is 6).
            cols (int): Number of columns in the game board (default is 7).
            player1_symbol (str): Symbol representing player 1's discs (default is 'X').
            player2_symbol (str): Symbol representing player 2's discs (default is 'O').

        Raises:
            ValueError: If the dimensions are less than 6 rows and 7 columns,
                        or if player symbols are the same.
        """
        
        # Validate dimensions
        if rows < 6 or cols < 7:
            raise ValueError("Dimensions must be at least 6 rows and 7 columns")

        # Validate player symbols
        if player1_symbol == player2_symbol:
            raise ValueError("Player symbols must be different")

        self.rows = rows
        self.cols = cols
        self.player1_symbol = player1_symbol
        self.player2_symbol = player2_symbol
        self.board = [[FourInLine.EMPTY_SPACE for _ in range(cols)] for _ in range(rows)]  # Initialize the game board

    def get_board_string(self, print_board=False):
        """
        Get the string representation of the game board.

        Args:
            print_board (bool, optional): Whether to print the board to the console (default is False).

        Returns:
            str: String representation of the game board.
        """

        board_str = '\n'.join(['|'.join(row) for row in self.board])
        if print_board:
            print(board_str)
        return board_str
    
    def make_move(self, player_symbol, column_selected):
        """
        Prompt the player to make a move and update the game board.

        Args:
            player_symbol (str): Symbol representing the current player's disc.
            column_selected (int): Column selected by the player (1-indexed).

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        # Validate the player's symbol
        if player_symbol != self.player1_symbol and player_symbol != self.player2_symbol:
            print("Invalid player symbol. Please use the correct player symbol.")
            return False

        # Validate the column selected by the player
        if column_selected < 1 or column_selected > self.cols:
            print("Invalid column number. Please choose a column within the valid range.")
            return False

        # Check if there is space available in the selected column
        if ' ' not in [row[column_selected - 1] for row in self.board]:
            print("Column is full. Please choose another column.")
            return False

        # Update the game board with the player's move
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][column_selected - 1] == FourInLine.EMPTY_SPACE:
                self.board[row][column_selected - 1] = player_symbol
                return True

        # This should never be reached if the previous checks are correct
        return False
    
    def check_win(self, player_symbol):
        """
        Check if the specified player has won the game.

        Args:
            player_symbol (str): Symbol representing the player's disc.

        Returns:
            list: List of positions where the player has won (empty list if the player has not won).
        """
        # Check for horizontal lines
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == player_symbol for i in range(4)):
                    return [(row, col + i) for i in range(4)]

        # Check for vertical lines
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if all(self.board[row + i][col] == player_symbol for i in range(4)):
                    return [(row + i, col) for i in range(4)]

        # Check for diagonal lines (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == player_symbol for i in range(4)):
                    return [(row + i, col + i) for i in range(4)]

        # Check for diagonal lines (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == player_symbol for i in range(4)):
                    return [(row - i, col + i) for i in range(4)]

        # No winning positions found
        return None
    
    def create_random_board(self, moves):
        """
        Fill the game board with a random sequence of moves.

        Args:
            moves (int): Number of moves to make.

        Returns:
            None
        """
        player_symbols = [self.player1_symbol, self.player2_symbol]
        for _ in range(moves):
            player_symbol = player_symbols[_ % 2]
            column_selected = random.randint(1, self.cols)
            self.make_move(player_symbol, column_selected)

    @staticmethod
    def get_id(board, empty_value='#'):
        """
        Concatenate all elements of the board into one string, replacing empty spaces with a specified value.

        Args:
            board (list): List of lists representing the game board.
            empty_value (str, optional): Value to replace empty spaces (default is '#').

        Returns:
            str: Concatenated string of all elements in the board.
        """
        return ''.join(''.join(empty_value if cell == FourInLine.EMPTY_SPACE else cell for cell in row) for row in board)
    

    @staticmethod
    def from_id(id_string, rows, cols, empty_value='#'):
        """
        Convert an ID string back to a game board represented as a list of lists.

        Args:
            id_string (str): ID string representing the game board.
            rows (int): Number of rows in the game board.
            cols (int): Number of columns in the game board.
            empty_value (str, optional): Value representing empty spaces (default is '#').

        Returns:
            list: List of lists representing the game board.

        Raises:
            ValueError: If the length of the ID string does not match the expected dimensions of the board
                        after replacing occurrences of empty_value with a single character placeholder.
        """
        
        expected_length = rows * cols
        if len(id_string) != expected_length + (len(empty_value) - 1) * id_string.count(empty_value):
            raise ValueError(f"Length of ID string ({len(id_string)}) does not match expected dimensions ({expected_length})")

        board = []
        for i in range(0, len(id_string), cols):
            row = []
            for j in range(cols):
                idx = i + j
                if id_string[idx:idx + len(empty_value)] == empty_value:
                    row.append(FourInLine.EMPTY_SPACE)
                else:
                    row.append(id_string[idx])
            board.append(row)
        return board