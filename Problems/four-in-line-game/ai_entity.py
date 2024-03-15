from game import FourInLine

class AIEntity:
    
    # Define constants for direction
    HORIZONTAL = 1
    VERTICAL = 2
    POSITIVE_DIAGONAL = 3
    NEGATIVE_DIAGONAL = 4
    
    def __init__(self, four_in_line, difficulty_level, player_symbol):
        """
        Initialize the AIEntity with the specified FourInLine object, difficulty level, and player symbol.

        Args:
            four_in_line (FourInLine): The FourInLine object representing the game.
            difficulty_level (int): The difficulty level of the AI (1 for easy, 2 for medium, 3 for hard).
            player_symbol (str): The symbol representing the AI player on the game board.
        """
        self.four_in_line = four_in_line
        self.difficulty_level = difficulty_level
        self.player_symbol = player_symbol

    def get_line(self, start, line_size, direction):
        """
        Get a line starting from the given position, moving in the specified direction.

        Args:
            start (tuple): The starting position (row, col).
            line_size (int): The size of the line to evaluate.
            direction (int): The direction to move (1 for horizontal, 2 for vertical,
                             3 for positive diagonal, 4 for negative diagonal).

        Returns:
            list: A list containing elements of the evaluated line.
        """
        row, col = start
        line = []

        # Determine the step size and direction
        if direction == AIEntity.HORIZONTAL:
            step_row, step_col = 0, 1
        elif direction == AIEntity.VERTICAL:
            step_row, step_col = 1, 0
        elif direction == AIEntity.POSITIVE_DIAGONAL:
            step_row, step_col = 1, 1
        elif direction == AIEntity.NEGATIVE_DIAGONAL:
            step_row, step_col = -1, 1
        else:
            raise ValueError("Invalid direction")

        # Move along the line and collect elements
        for _ in range(line_size):
            line.append(self.four_in_line.game_board()[row][col])
            row += step_row
            col += step_col

        return line
    
    def evaluate_board(self, symbol_player):
        """
        Evaluate the game board to find lines of the specified player's symbol.
        
        Args:
            symbol_player (str): Symbol representing the player's discs.

        Returns:
            list: List of objects representing lines found on the board. Each object contains
                  start_tuple, direction, and symbol_quantity.
        """
        lines_found = []

        for row in range(self.four_in_line.rows):
            for col in range(self.four_in_line.cols - 3):
                line = self.get_line(start=(row, col), line_size=4, direction=AIEntity.HORIZONTAL)
                
                if (line.count(symbol_player) >= 1 and line.count(symbol_player) + line.count(FourInLine.EMPTY_SPACE) == 4):
                    lines_found.append({
                        'start_tuple': (row, col),
                        'direction': AIEntity.HORIZONTAL,
                        'symbol_quantity': line.count(symbol_player)
                    })

        return lines_found
    
