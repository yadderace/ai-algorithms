from game import FourInLine
import random

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

    def get_line(self, board, start, line_size, direction):
        """
        Get a line starting from the given position, moving in the specified direction.

        Args:
            board (list of lists): The game board represented as a 2D list.
            start (tuple): The starting position (row, col).
            line_size (int): The size of the line to evaluate.
            direction (int): The direction to move (1 for horizontal, 2 for vertical,
                             3 for positive diagonal, 4 for negative diagonal).

        Returns:
            list: A list containing elements of the evaluated line.

        Raises:
            ValueError: If the direction is invalid.
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
            line.append(board[row][col])
            row += step_row
            col += step_col

        return line
    
    def get_possible_victory_lines(self, board, symbol_player):
        """
        Evaluate the game board to find lines of the specified player's symbol.

        Args:
            board (list of lists): The game board represented as a 2D list.
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
        rows = len(board)
        cols = len(board[0])
        lines_found = []

        # Evaluating the board horizontally
        for row in range(rows):
            for col in range(cols - 3):
                line = self.get_line(board=board, start=(row, col), line_size=4, direction=AIEntity.HORIZONTAL)
                
                if (line.count(symbol_player) >= 1 and line.count(symbol_player) + line.count(FourInLine.EMPTY_SPACE) == 4):
                    lines_found.append({
                        'start_tuple': (row, col),
                        'direction': AIEntity.HORIZONTAL,
                        'symbol_quantity': line.count(symbol_player)
                    })
        
        # Evaluating the board vertically
        for col in range(cols):
            for row in range(rows - 3):
                line = self.get_line(board=board, start=(row,col), line_size=4, direction=AIEntity.VERTICAL)

                if (line.count(symbol_player) >= 1 and line.count(symbol_player) + line.count(FourInLine.EMPTY_SPACE) == 4):
                    lines_found.append({
                        'start_tuple': (row, col),
                        'direction': AIEntity.VERTICAL,
                        'symbol_quantity': line.count(symbol_player)
                    })

        # Evaluating the board for negative diagonals
        for row in range(3, rows):
            for col in range(3, cols):
                line = self.get_line(board=board, start=(row, col), line_size=4, direction=AIEntity.NEGATIVE_DIAGONAL)

                if (line.count(symbol_player) >= 1 and line.count(symbol_player) + line.count(FourInLine.EMPTY_SPACE) == 4):
                    lines_found.append({
                        'start_tuple': (row, col),
                        'direction': AIEntity.NEGATIVE_DIAGONAL,
                        'symbol_quantity': line.count(symbol_player)
                    })

        # Evaluating the board for positive diagonals
        for row in range(3, rows):
            for col in range(cols - 3):
                line = self.get_line(board=board, start=(row, col), line_size=4, direction=AIEntity.POSITIVE_DIAGONAL)

                if (line.count(symbol_player) >= 1 and line.count(symbol_player) + line.count(FourInLine.EMPTY_SPACE) == 4):
                    lines_found.append({
                        'start_tuple': (row, col),
                        'direction': AIEntity.POSITIVE_DIAGONAL,
                        'symbol_quantity': line.count(symbol_player)
                    })

        return lines_found
    
    def calculate_board_value(self, board, symbol_player):
        """
        Calculate the value of the game board for the specified player.

        This function calculates the value of the game board for the specified player based on the lines where the player
        has the potential to achieve victory. The function iterates over all possible victory lines on the board and sums
        up the proportions of symbols owned by the player in each line. The total sum is divided by the number of lines
        found to get the average proportion of the player's symbols on the board.

        Args:
            board (list of lists): The game board represented as a 2D list.
            symbol_player (str): Symbol representing the player's discs.

        Returns:
            float: The calculated value of the game board for the specified player, ranging from 0.0 to 1.0.
        """
        victory_lines = self.get_possible_victory_lines(board=board, symbol_player=symbol_player)
        sum_proportion = 0.0
        
        for line in victory_lines:
            if line['symbol_quantity'] != 4:
                sum_proportion += (line['symbol_quantity'] / 4)
            elif line['symbol_quantity'] == 4:
                return 1.0
        return round(sum_proportion / len(victory_lines), 2)

    def make_virtual_move(self, board, column, symbol_player):
        """
        Make a virtual move for the specified player on the given board.

        This function adds the player's symbol to the top of the specified column in the board, simulating a move
        without modifying the original board.

        Args:
            board (list of lists): The game board represented as a 2D list.
            column (int): The column in which to make the move.
            symbol_player (str): Symbol representing the player's discs.

        Returns:
            list of lists: The new board after making the virtual move.
        """
        new_board = [row[:] for row in board]  # Create a deep copy of the board to avoid modifying the original

        # Find the top empty space in the specified column and place the player's symbol there
        for row in range(len(new_board) - 1, -1, -1):  # Start from the bottom row
            if new_board[row][column] == FourInLine.EMPTY_SPACE: 
                new_board[row][column] = symbol_player  
                break

        return new_board

    def get_best_move(self, board, player_symbol):
        """
        Determine the best move for the specified player on the given board.

        This function iterates over each column of the board and calculates the board value after making a move in each
        column. It then returns the column number that results in the highest board value. If there are multiple moves with
        the same highest value, it selects one randomly.

        Args:
            board (list of lists): The game board represented as a 2D list.
            player_symbol (str): Symbol representing the player's discs.

        Returns:
            int: The column number representing the best move for the specified player.
        """
        best_moves = []
        best_value = -1
        
        for col in range(len(board[0])):
            # Make a move in the current column
            new_board = self.make_virtual_move(board, col, player_symbol)
            
            # Calculate the board value after making the move
            board_value = self.calculate_board_value(new_board, player_symbol)

            # Check if the current move has a higher value than the best value found so far
            if board_value > best_value:
                best_moves = [(col,best_value)]  # If the current move is the best, update the list of best moves
                best_value = board_value
            elif board_value == best_value:
                best_moves.append((col,best_value))  # If the current move has the same value as the best, add it to the list of best moves

        # Randomly select one of the best moves
        best_move = random.choice(best_moves)
        return best_move[0], best_move[1]


def main():
    # Initialize the FourInLine game
    game = FourInLine()
    game.create_random_board(moves=15)
    print("Board is ready")
    print(game.get_board_string())
    
    ai_entity_x = AIEntity(four_in_line=game, difficulty_level=1, player_symbol='X')
    best_move, board_value = ai_entity_x.get_best_move(board=game.game_board, player_symbol='X')
    print(f"Best Move: {best_move}, Board Value: {board_value}")

    best_move, board_value = ai_entity_x.get_best_move(board=game.game_board, player_symbol='O')
    print(f"Best Move: {best_move}, Board Value: {board_value}")
    
if __name__ == "__main__":
    main()