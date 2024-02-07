from ChessBoard import ChessBoard  # Assuming your ChessBoard class is defined in chess_board.py

class Problem:
    def __init__(self, n_dim, n_queens):
        self.n_dim = n_dim
        self.n_queens = n_queens
        self.chess_board = ChessBoard(n_dim, n_queens)
        self.chess_board.place_queens()  # Place the queens
        self.current_state_identifier = self.chess_board.get_identifier()

    def print_current_state(self):
        print("Current State:")
        self.chess_board.print_board_from_identifier(self.current_state_identifier)

        next_moves = self.chess_board.get_queen_next_moves(3)
        for move in next_moves:
            print("=============================================")
            self.chess_board.print_board_from_identifier(move)
            print(f"Cost {self.chess_board.cost_queens(move)}")

# Example usage:
if __name__ == "__main__":
    n_dim = 8
    n_queens = 5
    problem_instance = Problem(n_dim, n_queens)
    problem_instance.print_current_state()

