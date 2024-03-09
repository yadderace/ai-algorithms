class FourInLine:
    DEFAULT_ROWS = 6
    DEFAULT_COLS = 7
    DEFAULT_PLAYER1_SYMBOL = 'X'
    DEFAULT_PLAYER2_SYMBOL = 'O'

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
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]  # Initialize the game board

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
            if self.board[row][column_selected - 1] == ' ':
                self.board[row][column_selected - 1] = player_symbol
                return True

        # This should never be reached if the previous checks are correct
        return False