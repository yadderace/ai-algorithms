from queue import Queue, PriorityQueue
from CustomStructures.MyTree import MyTree

import AIAlgorithms.utils as utils


def simple_treesearch(problem, space):

    initial_state_node = space.nodes[problem['init_state_id']]
    goal_state_id = problem['end_state_id']
    
    # Initializing the frontier adding expanded nodes of initial state
    if initial_state_node == None:
        return { 'error': True, 'message': 'The initial state does not exist', 'solution': None }
    frontier = Queue()
    [frontier.put(space.nodes[neighbor]['data']) for neighbor in space.neighbors(initial_state_node['data'].node_id)]
    
    while True:

        # If frontier is empty there's no solution
        if frontier.qsize() == 0:
            return { 'error': True, 'message': 'There is not solution', 'solution': None }
        
        # Validating if the next node of frontier is the goal
        leaf_node = frontier.get()
        print(f'Passing through Node ID: {leaf_node.node_id}, attributes: {leaf_node.custom_attributes}')
        if leaf_node.node_id == goal_state_id:
            return { 'error': False, 'message': 'Solution Found', 'solution': leaf_node}
        
        # Expanding leaf node and adding them to the frontier
        [frontier.put(space.nodes[neighbor]['data']) for neighbor in space.neighbors(leaf_node.node_id)]


def simple_graphsearch(problem, space):

    initial_state_node = space.nodes[problem['init_state_id']]
    goal_state_id = problem['end_state_id']
    
    # Initializing the frontier adding expanded nodes of initial state
    if initial_state_node == None:
        return { 'error': True, 'message': 'The initial state does not exist', 'solution': None }
    frontier = Queue()
    [frontier.put(neighbor) for neighbor in space.neighbors(initial_state_node['data'].node_id)]

    explored_nodes = []
    

    while True:
        
        # If frontier is empty there's no solution
        if frontier.qsize() == 0:
            return { 'error': True, 'message': 'There is not solution', 'solution': None }
        
        # Validating if the next node of frontier is the goal
        leaf_node = space.nodes[frontier.get()]['data']
        print(f'Passing through Node ID: {leaf_node.node_id}, attributes: {leaf_node.custom_attributes}')
        if leaf_node.node_id == goal_state_id:
            return { 'error': False, 'message': 'Solution Found', 'solution': leaf_node}
        
        # Adding the leaf_node to explored nodes
        explored_nodes.append(leaf_node.node_id)

        # Expanding leaf node and adding them to the frontier if the node isn't in the explored nodes or frontier
        [frontier.put(neighbor) for neighbor in space.neighbors(leaf_node.node_id) if (neighbor not in explored_nodes) and (neighbor not in list(frontier.queue))]


def breadth_first_search(problem, space):

    initial_state_node = space.nodes[problem['init_state_id']]['data']
    goal_state_id = problem['end_state_id']

    # Validating if initial state is goal node
    if(initial_state_node.node_id == goal_state_id):
        return { 'error': False, 'message': 'Solution Found', 'solution': initial_state_node}
    
    # Initializing frontier and explored nodes
    frontier = Queue()
    frontier.put(initial_state_node)
    explored_nodes = []
    
    while True:

        # Validating if there's any node in the frontier
        if frontier.qsize() == 0:
            return { 'error': True, 'message': 'There is not solution', 'solution': None }
        
        # Getting a node to validate from the frontier
        current_node = frontier.get()
        explored_nodes.append(current_node)

        # Passing through leaf nodes from current_node
        for child_node_id in space.neighbors(current_node.node_id):
            
            leaf_node = space.nodes[child_node_id]['data']
            if(leaf_node.node_id not in [n.node_id for n in explored_nodes]) and (leaf_node.node_id not in [n.node_id for n in list(frontier.queue)]):
                
                print(f'Passing through Node ID: {leaf_node.node_id}, attributes: {leaf_node.custom_attributes}')
                if(leaf_node.node_id == goal_state_id):
                    return { 'error': False, 'message': 'Solution Found', 'solution': leaf_node}
                
                frontier.put(leaf_node)


def uniform_cost_search(problem, space):
    
    initial_state_node = space.nodes[problem['init_state_id']]['data']
    goal_state_id = problem['end_state_id']

    # Initializing frontier and explored nodes
    frontier = PriorityQueue()
    frontier.put((0, initial_state_node))
    explored_nodes = []

    while True:

        # Validating if there's any node in the frontier
        if frontier.qsize() == 0:
            return { 'error': True, 'message': 'There is not solution', 'solution': None }
        
        # Getting a node to validate from the frontier
        priority, current_node = frontier.get()
        
        # Validating if it's the goal node
        print(f'Passing through Node ID: {current_node.node_id}, attributes: {current_node.custom_attributes}')
        if(current_node.node_id == goal_state_id):
            return { 'error': False, 'message': 'Solution Found', 'solution': current_node}
        
        explored_nodes.append(current_node)

        # Passing through leaf nodes from current_node
        for child_node_id in space.neighbors(current_node.node_id):
            leaf_node = space.nodes[child_node_id]['data']
            step_cost = space.get_edge_data(current_node.node_id, leaf_node.node_id)['weight']
            path_cost = current_node.path_cost + step_cost
            
            # Adding leaf node to frontier if it wasn't added to explored or frontier
            if(leaf_node.node_id not in [n.node_id for n in explored_nodes]) and (leaf_node.node_id not in [n.node_id for p,n in list(frontier.queue)]):
                leaf_node.path_cost = path_cost
                frontier.put((path_cost, leaf_node))
            
            # Replacing node in frontier if path cost is lower
            elif (leaf_node.node_id in [n.node_id for p,n in list(frontier.queue)]) and (path_cost < utils.peek_from_queue(frontier, leaf_node.node_id).path_cost):
                utils.peek_from_queue(frontier, leaf_node.node_id).path_cost = path_cost
                utils.update_priority(frontier, leaf_node.node_id, path_cost)


def recursive_depth_limited_search(node, problem, space, limit):
    goal_state_id = problem['end_state_id']

    print(f'Passing through Node ID: {node.node_id}, attributes: {node.custom_attributes}')
    if(node.node_id == goal_state_id):
        return { 'cutoff': False, 'failure': False, 'solution': node}
    
    elif(limit == 0):
        print("Limit Reached")
        return { 'cutoff': True, 'failure': False, 'solution': None }
    
    else:
        cutoff_ocurred = False

        # Passing through child nodes from current_node
        for child_node_id in space.neighbors(node.node_id): 
            child_node = space.nodes[child_node_id]['data']
            result = recursive_depth_limited_search(child_node, problem, space, limit - 1)
            
            # Validating if it reached the limit
            if(result['cutoff']):
                cutoff_ocurred = True
            elif(not result['failure']):
                return result
            
        if cutoff_ocurred:
            return { 'cutoff': True, 'failure': False, 'solution': None }
        else:
            return { 'cutoff': True, 'failure': True, 'solution': None }


def depth_limited_search(problem, space, limit = None):

    initial_state_node = space.nodes[problem['init_state_id']]['data']

    return recursive_depth_limited_search(initial_state_node, problem, space, limit)


def greedy_best_first_search(problem, space):

    initial_state_node = space.nodes[problem['init_state_id']]['data']
    goal_state_id = problem['end_state_id']

    # Initializing frontier and explored nodes
    frontier = PriorityQueue()
    frontier.put((0, initial_state_node))
    explored_nodes = []

    while True:

        # Validating if there's any node in the frontier
        if frontier.qsize() == 0:
            return { 'error': True, 'message': 'There is not solution', 'solution': None }
        
        # Getting a node to validate from the frontier
        priority, current_node = frontier.get()
        
        # Validating if it's the goal node
        print(f'Passing through Node ID: {current_node.node_id}, attributes: {current_node.custom_attributes}')
        if(current_node.node_id == goal_state_id):
            return { 'error': False, 'message': 'Solution Found', 'solution': current_node}
        
        explored_nodes.append(current_node)

        # Passing through leaf nodes from current_node
        for child_node_id in space.neighbors(current_node.node_id):
            leaf_node = space.nodes[child_node_id]['data']
            
            # Adding leaf node to frontier if it wasn't added to explored or frontier
            if(leaf_node.node_id not in [n.node_id for n in explored_nodes]) and (leaf_node.node_id not in [n.node_id for p,n in list(frontier.queue)]):
                frontier.put((leaf_node.informed_heuristic, leaf_node))


def a_star_search(problem, space):
    initial_state_node = space.nodes[problem['init_state_id']]['data']
    goal_state_id = problem['end_state_id']

    # Initializing frontier and explored nodes
    frontier = PriorityQueue()
    frontier.put((0, initial_state_node))
    explored_nodes = []

    while True:

        # Validating if there's any node in the frontier
        if frontier.qsize() == 0:
            return { 'error': True, 'message': 'There is not solution', 'solution': None }
        
        # Getting a node to validate from the frontier
        priority, current_node = frontier.get()
        
        # Validating if it's the goal node
        print(f'Passing through Node ID: {current_node.node_id}, Estimated Cost: {current_node.estimated_cost}, attributes: {current_node.custom_attributes}')
        if(current_node.node_id == goal_state_id):
            return { 'error': False, 'message': 'Solution Found', 'solution': current_node}
        
        explored_nodes.append(current_node)

        # Passing through leaf nodes from current_node
        for child_node_id in space.neighbors(current_node.node_id):
            leaf_node = space.nodes[child_node_id]['data']
            step_cost = space.get_edge_data(current_node.node_id, leaf_node.node_id)['weight']
            g_cost = current_node.path_cost + step_cost # Path Cost
            h_cost = leaf_node.informed_heuristic # Heuristic Cost
            print(f"Name: {leaf_node.custom_attributes['name']}, step_cost: {step_cost}, g_cost: {g_cost}, h_cost: {h_cost}")
            f_cost = g_cost + h_cost

            
            # Adding leaf node to frontier if it wasn't added to explored or frontier
            if(leaf_node.node_id not in [n.node_id for n in explored_nodes]) and (leaf_node.node_id not in [n.node_id for p,n in list(frontier.queue)]):
                leaf_node.estimated_cost = f_cost
                leaf_node.path_cost = g_cost
                frontier.put((f_cost, leaf_node))
            
            # Replacing node in frontier if path cost is lower
            elif (leaf_node.node_id in [n.node_id for p,n in list(frontier.queue)]) and (f_cost < utils.peek_from_queue(frontier, leaf_node.node_id).estimated_cost):
                utils.peek_from_queue(frontier, leaf_node.node_id).estimated_cost = f_cost
                utils.update_priority(frontier, leaf_node.node_id, f_cost)

def recursive_iterative_a_star_search(node, problem, space, limit):
    
    goal_state_id = problem['end_state_id']
    # Validating if it's the goal node
    print(f'Passing through Node ID: {node.node_id}, attributes: {node.custom_attributes}')
    if(node.node_id == goal_state_id):
        return { 'error': False, 'message': 'Solution Found', 'solution': node }
    
    successors = []
    # Passing through leaf nodes from current_node
    for child_node_id in space.neighbors(node.node_id):
        leaf_node = space.nodes[child_node_id]['data']
        successors.append(leaf_node)
    
    for node_successor in successors:
        step_cost = space.get_edge_data(node_successor.node_id, node.node_id)['weight']
        g_cost = node.path_cost + step_cost # Path Cost
        h_cost = node_successor.informed_heuristic # Heuristic Cost
        f_cost = g_cost + h_cost
        node_successor.estimated_cost = max(f_cost, node.estimated_cost)
        node_successor.path_cost = g_cost

    while True:
        best_node = min(successors, key=lambda suc: suc.estimated_cost)
        if(best_node.estimated_cost > limit):
            return { 'error': True, 'message': 'Solution No Found', 'solution': None }
        
        sorted_successors = sorted(successors, key=lambda suc: suc.estimated_cost)
        second_best_node = sorted_successors[1]

        result = recursive_iterative_a_star_search(best_node, problem, space, min(second_best_node.estimated_cost, limit))

        if not result['error']:
            return result

def iterative_a_star_search(problem, space):
    initial_state_node = space.nodes[problem['init_state_id']]['data']
    
    my_tree_search = MyTree()
    my_tree_search.create_node('Root', identifier=initial_state_node.node_id, g_cost=0, h_cost=initial_state_node.informed_heuristic)
    
    print(my_tree_search.get_node(initial_state_node.node_id))
    # recursive_iterative_a_star_search(initial_state_node, problem, space, 10000000)