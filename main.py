import CustomStructures.MyGraph as cg
import AIAlgorithms.treesearch as ai_alg


# ========================================== [DEFINING SPACE]

def creating_graph():

    problem_space = cg.MyGraph()
    problem_space.add_node(1, custom_attributes={'name': 'Oradea', 'informed_heuristic': 380})
    problem_space.add_node(2, custom_attributes={'name': 'Zerind', 'informed_heuristic': 374})
    problem_space.add_node(3, custom_attributes={'name': 'Arad', 'informed_heuristic': 366})
    problem_space.add_node(4, custom_attributes={'name': 'Timisoara', 'informed_heuristic': 329})
    problem_space.add_node(5, custom_attributes={'name': 'Lugoj', 'informed_heuristic': 244})
    problem_space.add_node(6, custom_attributes={'name': 'Mehadia', 'informed_heuristic': 241})
    problem_space.add_node(7, custom_attributes={'name': 'Drobeta', 'informed_heuristic': 242})
    problem_space.add_node(8, custom_attributes={'name': 'Sibiu', 'informed_heuristic': 253})
    problem_space.add_node(9, custom_attributes={'name': 'Rimnicu Vilcea', 'informed_heuristic': 193})
    problem_space.add_node(10, custom_attributes={'name': 'Craiova', 'informed_heuristic': 160})
    problem_space.add_node(11, custom_attributes={'name': 'Fagaras', 'informed_heuristic': 176})
    problem_space.add_node(12, custom_attributes={'name': 'Pitesti', 'informed_heuristic': 100})
    problem_space.add_node(13, custom_attributes={'name': 'Bucharest', 'informed_heuristic': 0})
    problem_space.add_node(14, custom_attributes={'name': 'Giurgiu', 'informed_heuristic': 77})
    problem_space.add_node(15, custom_attributes={'name': 'Neamt', 'informed_heuristic': 234})
    problem_space.add_node(16, custom_attributes={'name': 'Iasi', 'informed_heuristic': 226})
    problem_space.add_node(17, custom_attributes={'name': 'Vasliu', 'informed_heuristic': 199})
    problem_space.add_node(18, custom_attributes={'name': 'Urziceni', 'informed_heuristic': 80})
    problem_space.add_node(19, custom_attributes={'name': 'Hirsova', 'informed_heuristic': 151})
    problem_space.add_node(20, custom_attributes={'name': 'Eforie', 'informed_heuristic': 161})

    problem_space.add_edges_from([(1,2), (1,8)])
    problem_space[1][2]['weight'] = 71
    problem_space[1][8]['weight'] = 151

    problem_space.add_edges_from([(2,3)])
    problem_space[2][3]['weight'] = 75

    problem_space.add_edges_from([(3,4), (3,8)])
    problem_space[3][4]['weight'] = 118
    problem_space[3][8]['weight'] = 140

    problem_space.add_edges_from([(4,5)])
    problem_space[4][5]['weight'] = 111

    problem_space.add_edges_from([(5,6)])
    problem_space[5][6]['weight'] = 70

    problem_space.add_edges_from([(6,7)])
    problem_space[6][7]['weight'] = 75

    problem_space.add_edges_from([(7,10)])
    problem_space[7][10]['weight'] = 120

    problem_space.add_edges_from([(8,9), (8,11)])
    problem_space[8][9]['weight'] = 80
    problem_space[8][11]['weight'] = 99

    problem_space.add_edges_from([(9,10), (9, 12)])
    problem_space[9][10]['weight'] = 146
    problem_space[9][12]['weight'] = 97

    problem_space.add_edges_from([(10,12)])
    problem_space[10][12]['weight'] = 138

    problem_space.add_edges_from([(11,13)])
    problem_space[11][13]['weight'] = 211

    problem_space.add_edges_from([(12,13)])
    problem_space[12][13]['weight'] = 101

    problem_space.add_edges_from([(13,14), (13,18)])
    problem_space[13][14]['weight'] = 90
    problem_space[13][18]['weight'] = 85

    problem_space.add_edges_from([(15,16)])
    problem_space[15][16]['weight'] = 87

    problem_space.add_edges_from([(16,17)])
    problem_space[16][17]['weight'] = 92

    problem_space.add_edges_from([(17,18)])
    problem_space[17][18]['weight'] = 142

    problem_space.add_edges_from([(18,19)])
    problem_space[18][19]['weight'] = 98

    problem_space.add_edges_from([(19,20)])
    problem_space[19][20]['weight'] = 86

    return problem_space

# ========================================== [SIMPLE TREE SEARCH]
print("======================== [Simple Tree Search]")
problem = {
    'init_state_id': 3,
    'end_state_id': 13
}
problem_space = creating_graph()
print(f"Problem: {problem}")
solution = ai_alg.simple_treesearch(problem=problem, space=problem_space)
print(f"Solution {solution}")

# ========================================== [SIMPLE GRAPH SEARCH]
print("======================== [Simple Graph Search]")
problem = {
    'init_state_id': 3,
    'end_state_id': 13
}
problem_space = creating_graph()
print(f"Problem: {problem}")
solution = ai_alg.simple_graphsearch(problem=problem, space=problem_space)
print(f"Solution {solution}")

# ========================================== [BREADTH FIRST SEARCH]
print("======================== [Breadth First Search]")
problem = {
    'init_state_id': 3,
    'end_state_id': 13
}
problem_space = creating_graph()
print(f"Problem: {problem}")
solution = ai_alg.breadth_first_search(problem=problem, space=problem_space)
print(f"Solution {solution}")


# ========================================== [UNIFORM COST SEARCH]
print("======================== [Uniform Cost Search]")
problem = {
    'init_state_id': 3,
    'end_state_id': 10
}
problem_space = creating_graph()
print(f"Problem: {problem}")
solution = ai_alg.uniform_cost_search(problem=problem, space=problem_space)
print(f"Solution {solution}")

# ========================================== [DEPTH LIMITED SEARCH]
print("======================== [Depth Limited Search]")
problem = {
    'init_state_id': 3,
    'end_state_id': 10
}
problem_space = creating_graph()
print(f"Problem: {problem}")
result = ai_alg.depth_limited_search(problem=problem, space=problem_space, limit=5)
print(f"Solution {result}")

# ========================================== [GREEDY BEST FIRST SEARCH]
# This is an informed search. The heuristic is in the attribute informed_heuristic in each node
print("======================== [Greedy Best First Search]")
problem = {
    'init_state_id': 3,
    'end_state_id': 13 # This state should have 0 as informed heuristic because is the goal
}
problem_space = creating_graph()
print(f"Problem: {problem}")
result = ai_alg.greedy_best_first_search(problem=problem, space=problem_space)
print(f"Solution {result}")


# ========================================== [A* SEARCH]
# This is an informed search. The heuristic is in the attribute informed_heuristic in each node and its added to path cost to get an estimation
print("======================== [Greedy Best First Search]")
problem = {
    'init_state_id': 3,
    'end_state_id': 13 # This state should have 0 as informed heuristic because is the goal
}
problem_space = creating_graph()
print(f"Problem: {problem}")
result = ai_alg.a_star_search(problem=problem, space=problem_space)
print(f"Solution {result}")


# ========================================== [ITERATIVE A* SEARCH]
# This is an informed search. The heuristic is in the attribute informed_heuristic in each node and its added to path cost to get an estimation. It is recursive
print("======================== [Iterative A* Search]")
problem = {
    'init_state_id': 3,
    'end_state_id': 13 # This state should have 0 as informed heuristic because is the goal
}
problem_space = creating_graph()
print(f"Problem: {problem}")
result = ai_alg.iterative_a_star_search(problem=problem, space=problem_space)
print(f"Solution {result}")

