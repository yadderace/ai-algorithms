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
            step_row, step_col = -1, 1
        elif direction == AIEntity.NEGATIVE_DIAGONAL:
            step_row, step_col = -1, -1
        else:
            raise ValueError("Invalid direction")

        # Move along the line and collect elements
        for _ in range(line_size):
            line.append(self.four_in_line.game_board[row][col])
            row += step_row
            col += step_col

        return line
    
    def evaluate_board(self):
        """
        Evaluate the game board to find lines of the specified player's symbol.
        
        Args:
            symbol_player (str): Symbol representing the player's discs.

        Returns:
            list: List of objects representing lines found on the board. Each object contains
                start_tuple, direction, and symbol_quantity.

        The function evaluates the board horizontally, vertically, and diagonally (both positive and negative)
        to identify lines of the specified player's symbol. The lines must contain at least one symbol of the player
        and may include empty spaces ('.') in a sequence of four. Each line is represented as an object containing
        the following attributes:
        
        - start_tuple (tuple): The starting position of the line as a tuple (row, col).
        - direction (str): The direction of the line ('horizontal', 'vertical', 'positive_diagonal', 'negative_diagonal').
        - symbol_quantity (int): The number of symbols of the player found in the line.
        """
        symbol_player = self.player_symbol
        lines_found = []

        # Evaluating the board horizontally
        for row in range(self.four_in_line.rows):
            for col in range(self.four_in_line.cols - 3):
                line = self.get_line(start=(row, col), line_size=4, direction=AIEntity.HORIZONTAL)
                
                if (line.count(symbol_player) >= 1 and line.count(symbol_player) + line.count(FourInLine.EMPTY_SPACE) == 4):
                    lines_found.append({
                        'start_tuple': (row, col),
                        'direction': AIEntity.HORIZONTAL,
                        'symbol_quantity': line.count(symbol_player)
                    })
        
        # Evaluating the board vertically
        for col in range(self.four_in_line.cols):
            for row in range(self.four_in_line.rows - 3):
                line = self.get_line(start=(row,col), line_size=4, direction=AIEntity.VERTICAL)

                if (line.count(symbol_player) >= 1 and line.count(symbol_player) + line.count(FourInLine.EMPTY_SPACE) == 4):
                    lines_found.append({
                        'start_tuple': (row, col),
                        'direction': AIEntity.VERTICAL,
                        'symbol_quantity': line.count(symbol_player)
                    })

        # Evaluating the board for negative diagonals
        for row in range(3, self.four_in_line.rows):
            for col in range(3, self.four_in_line.cols):
                line = self.get_line(start=(row, col), line_size=4, direction=AIEntity.NEGATIVE_DIAGONAL)

                if (line.count(symbol_player) >= 1 and line.count(symbol_player) + line.count(FourInLine.EMPTY_SPACE) == 4):
                    lines_found.append({
                        'start_tuple': (row, col),
                        'direction': AIEntity.NEGATIVE_DIAGONAL,
                        'symbol_quantity': line.count(symbol_player)
                    })

        # Evaluating the board for positive diagonals
        for row in range(3, self.four_in_line.rows):
            for col in range(self.four_in_line.cols - 3):
                line = self.get_line(start=(row, col), line_size=4, direction=AIEntity.POSITIVE_DIAGONAL)

                if (line.count(symbol_player) >= 1 and line.count(symbol_player) + line.count(FourInLine.EMPTY_SPACE) == 4):
                    lines_found.append({
                        'start_tuple': (row, col),
                        'direction': AIEntity.POSITIVE_DIAGONAL,
                        'symbol_quantity': line.count(symbol_player)
                    })

        return lines_found



def main():
    # Initialize the FourInLine game
    game = FourInLine()
    game.create_random_board(moves=15)
    print("Board is ready")
    print(game.get_board_string())
    
    ai_entity_x = AIEntity(four_in_line=game, difficulty_level=1, player_symbol='X')
    list_x = ai_entity_x.evaluate_board()
    print(list_x)

if __name__ == "__main__":
    main()