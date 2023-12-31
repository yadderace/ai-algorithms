from queue import Queue

frontier = Queue()
def simple_treesearch(problem, space):

    # Initializing the frontier
    print(problem['init_state_id'])
    initial_state_node = space.nodes[problem['init_state_id']]
    print(initial_state_node)
    if initial_state_node == None:
        return { 'error': True, 'message': 'The initial state does not exist', 'solution': None }
    
    # Adding neighbor nodes to the frontier
    [frontier.put(space.nodes[neighbor]['data']) for neighbor in space.neighbors(initial_state_node['data'].node_id)]
    
    goal_state_id = problem['end_state_id']
    
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
        

        