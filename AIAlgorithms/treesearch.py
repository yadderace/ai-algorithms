from queue import Queue, PriorityQueue

import utils

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
        for child_node_id in space.neighbors(current_node):
            
            leaf_node = space.nodes[child_node_id]['data']
            if(leaf_node.node_id not in explored_nodes) and (leaf_node.node_id not in list(frontier.queue)):
                
                print(f'Passing through Node ID: {leaf_node.node_id}, attributes: {leaf_node.custom_attributes}')
                if(leaf_node.node_id == goal_state_id):
                    return { 'error': False, 'message': 'Solution Found', 'solution': leaf_node}
                
                frontier.put(leaf_node.node_id)

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
        current_node = frontier.get()[1]

        # Validating if it's the goal node
        print(f'Passing through Node ID: {current_node.node_id}, attributes: {current_node.custom_attributes}')
        if(current_node.node_id == goal_state_id):
            return { 'error': False, 'message': 'Solution Found', 'solution': current_node}
        
        explored_nodes.append(current_node)

        # Passing through leaf nodes from current_node
        for child_node_id in space.neighbors(current_node):
            leaf_node = space.nodes[child_node_id]['data']

            # Adding leaf node to frontier if it wasn't added to explored or frontier
            if(leaf_node.node_id not in [n.node_id for n in explored_nodes]) and (leaf_node.node_id not in [n.node_id for n in list(frontier.queue)]):
                step_cost = space.get_edge_data(current_node.node_id, leaf_node.node_id)['weight']
                frontier.put((step_cost, leaf_node))
            
            # Replacing node in frontier if step cost is lower
            elif (leaf_node.node_id in [n.node_id for n in list(frontier.queue)]) and :


        
