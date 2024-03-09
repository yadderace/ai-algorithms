import random, math

from ChessBoard import ChessBoard  # Assuming your ChessBoard class is defined in chess_board.py

from CustomStructures import MyTree

class Problem:
    
    def __init__(self, n_dim, n_queens):
        self.n_dim = n_dim
        self.n_queens = n_queens

        # Those will be initialized when the board start
        self.chess_board = None
        self.tree_space = None
        self.current_node = None
        
    def start_board(self):
        # Initializing the board
        self.chess_board = ChessBoard(self.n_dim, self.n_queens)
        self.chess_board.place_queens()  # Place the queens
        current_state_identifier = self.chess_board.get_identifier()
        
        # Creating the tree
        self.tree_space = MyTree()
        self.current_node = self.tree_space.create_node('Root', node_id=current_state_identifier, g_cost=0, h_cost=1000000)
    
    def print_current_state(self):
        self.chess_board.print_board_from_identifier(self.current_node.node_id)

    def print_state_from_identifier(self, identifier):
        self.chess_board.print_board_from_identifier(identifier)

    def create_child_nodes(self, tree_node=None, max_spaces = 1):
        
        if(tree_node is None):
            tree_node = self.tree_space.get_node(self.current_node.identifier)
        
        child_objects = []
        
        # Iterates through each queen
        for i in range(1, self.n_queens + 1):
            queen_next_moves = self.chess_board.get_queen_next_moves(i, max_spaces)
            
            
            for move in queen_next_moves:
                
                # Calculates the cost for the new state
                new_cost = self.chess_board.cost_queens(move['identifier'])

                # Appends the alternative identifier and cost to the list of child nodes
                child_objects.append({'alternative_identifier': move['identifier'], 'cost': new_cost, 'queen': move['queen'], 'direction': move['direction'], 'steps': move['steps']})
                
                # Creates a child on the tree
                self.tree_space.create_node('Child', node_id=move['identifier'], parent=tree_node.identifier, g_cost=0, h_cost=new_cost)

        return child_objects

    def execute_action(self, action_identifier, queen_number, direction, steps):
        
        # Executes the movement in the board
        self.chess_board.move_queen(queen_number, direction, steps)

        # Updating the current node
        self.current_node = self.current_node.get_child_node(node_id = action_identifier)

    def get_stats(self, tree_node):
        level_node = self.tree_space.level(tree_node.identifier)
        tree_nodes = self.tree_space.size()

        return {'level_node': level_node, 'tree_nodes': tree_nodes}

    def hill_climbing_search(self, print_actions=False, print_board=False, limit_stuck_steps = 10 , max_spaces = 1):

        if(self.tree_space is None):
            return None
        
        # Variable used to avoid getting stuck
        stuck_steps = 0
        
        # Get the node for the initial state as set it as the current_node
        current_node = self.current_node

        while True:
            # Get all the childs from the current_state and select the one with the lowest cost
            childs = self.create_child_nodes(current_node ,max_spaces)
            best_child = min(childs, key=lambda suc: suc['cost'])

            # If it founds the minimum cost it should return the solution
            if (current_node.f_cost == 0):
                return {'last_node': current_node, 'found_solution': True, 'got_stuck': False }
            
            # If all the other childs have higher cost it should return the current node
            elif (best_child['cost'] > current_node.f_cost):
                return {'last_node': current_node, 'found_solution': False, 'got_stuck': False }
            
            # If the best child has the same cost, it moves to that child but will increase the stuck steps
            elif (current_node.f_cost == best_child['cost']) & (stuck_steps < limit_stuck_steps):
                stuck_steps += 1
            
            # If the quantity of stuck steps reached the limit the it will return the current node
            elif (stuck_steps == limit_stuck_steps):
                return {'last_node': current_node, 'found_solution': False, 'got_stuck': True }
            
            # Else, just restart the stuck steps because there's an optimal option
            else:
                stuck_steps = 0
            
            # Executes the action for the best child
            self.execute_action(action_identifier=best_child['alternative_identifier'], queen_number=best_child['queen'], direction=best_child['direction'], steps=best_child['steps'])
            current_node = self.current_node

            if(print_actions == True):
                print(f"--->")
                print(f"Cost: {self.chess_board.cost_queens(best_child['alternative_identifier'])}")
                print(f"Action: {best_child}")
            if(print_board == True):
                self.print_current_state()

    def action_acceptance(diff_energy = 0, temperature = 0):
        r = random.random()
        if(r < math.exp((diff_energy * -1)/temperature)):
            return True
        return False

    def simmulated_annealing(self, alpha_cool = 0.9, initial_temperature = 100, min_temperature = 1, initial_energy = 100, min_energy = 0, max_spaces = 1, limit_stuck_steps = 10, print_actions=False, print_board = True):
        
        # Get the node for the initial state as set it as the current_node
        current_node = self.current_node

        # Setting the max value of temperature
        current_temperature = initial_temperature

        # Seting the current energy
        current_energy = initial_energy

        # Setting initial stuck steps
        stuck_steps = 0

        while (current_temperature > min_temperature) and (current_energy > min_energy):

            # Get all the childs from the current_state and select the ones with the lowest cost
            childs = self.create_child_nodes(current_node ,max_spaces)
            min_cost = min(child['cost'] for child in childs)
            best_childs = [child for child in childs if child['cost'] == min_cost]
            
            # From best child selects a random child
            best_child = random.choice(best_childs) 

            # Calculating difference of energy
            diff_energy = current_energy - min_cost
            if(diff_energy == 0):
                stuck_steps += 1
            else:
                stuck_steps = 0
            
            if(min_cost == 0):
                return {'last_node': current_node, 'found_solution': True, 'got_stuck': False}

            if(stuck_steps == limit_stuck_steps):
                return {'last_node': current_node, 'found_solution': False, 'got_stuck': True }
            
            if(Problem.action_acceptance(diff_energy, current_temperature)):
                
                # Executes the action for the best child
                self.execute_action(action_identifier=best_child['alternative_identifier'], queen_number=best_child['queen'], direction=best_child['direction'], steps=best_child['steps'])
                current_node = self.current_node

                if(print_actions == True):
                    print(f"--->")
                    print(f"Cost: {self.chess_board.cost_queens(best_child['alternative_identifier'])}")
                    print(f"Action: {best_child}")
                if(print_board == True):
                    self.print_current_state()
                current_energy = min_cost

            
            current_temperature = current_temperature / alpha_cool
        
        return {'last_node': current_node, 'found_solution': False, 'got_stuck': False }
        



# Example usage:
# if __name__ == "__main__":
#     n_dim = 8
#     n_queens = 8
#     problem_instance = Problem(n_dim, n_queens)
    
#     problem_instance.start_board()
#     problem_instance.print_current_state()

#     #print("===================== [Hill Climbing Search]")
#     #problem_instance.hill_climbing_search(print_actions=True, print_board=True, max_spaces=n_dim)

#     print("===================== [Simmulated Annealing Search]")
#     problem_instance.simmulated_annealing(print_actions=True, print_board=True, max_spaces=n_dim)