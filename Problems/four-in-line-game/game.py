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
    

if __name__ == "__main__":
    # Initialize the game
    game = FourInLine()

    # Game loop
    current_player = 1
    while True:
        # Display the current game board
        board_string = game.get_board_string()
        print(board_string)

        # Determine the symbol of the current player
        player_symbol = game.player1_symbol if current_player == 1 else game.player2_symbol

        # Prompt the current player to make a move
        while True:
            column_selected = input(f"Player {current_player}, please choose a column (1-{game.cols}): ")
            try:
                column_selected = int(column_selected)
                break
            except ValueError:
                print("Invalid input. Please enter a valid column number.")

        # Make the move
        if game.make_move(player_symbol, column_selected):
            # Check if the current player has won
            if game.check_win(player_symbol):
                print(f"Player {current_player} wins!")
                break

            # Check for a draw
            if all(' ' not in row for row in game.board):
                print("It's a draw!")
                break

            # Switch to the next player
            current_player = 1 if current_player == 2 else 2
        else:
            print("Invalid move. Please try again.")