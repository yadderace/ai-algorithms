from queue import Queue

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