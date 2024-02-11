from ChessBoard import ChessBoard  # Assuming your ChessBoard class is defined in chess_board.py

from CustomStructures import MyTree

class Problem:
    
    def __init__(self, n_dim, n_queens):
        self.n_dim = n_dim
        self.n_queens = n_queens
        

    def start_board(self):
        # Initializing the board
        self.chess_board = ChessBoard(n_dim, n_queens)
        self.chess_board.place_queens()  # Place the queens
        current_state_identifier = self.chess_board.get_identifier()
        
        # Creating the tree
        self.tree_space = MyTree()
        self.current_node = self.tree_space.create_node('Root', node_id=current_state_identifier, g_cost=0, h_cost=0)
    

    def print_current_state(self):
        self.chess_board.print_board_from_identifier(self.current_node.node_id)

    def create_child_nodes(self, tree_node=None):
        
        if(tree_node is None):
            tree_node = self.tree_space.get_node(self.current_node.identifier)
        
        child_objects = []
        
        # Iterate through each queen
        for i in range(1, self.n_queens + 1):
            queen_next_moves = self.chess_board.get_queen_next_moves(i)
            
            
            for next_identifier in queen_next_moves:
                # Calculate the cost for the new state
                new_cost = self.chess_board.cost_queens(next_identifier)

                # Append the alternative identifier and cost to the list of child nodes
                child_objects.append({'alternative_identifier': next_identifier, 'cost': new_cost})
                
                # Create a child on the tree
                self.tree_space.create_node('Child', node_id=next_identifier, parent=tree_node.identifier, g_cost=0, h_cost=new_cost)

        return child_objects

# Example usage:
if __name__ == "__main__":
    n_dim = 8
    n_queens = 8
    problem_instance = Problem(n_dim, n_queens)
    
    problem_instance.start_board()
    problem_instance.print_current_state()

    list_next_moves = problem_instance.create_child_nodes()


