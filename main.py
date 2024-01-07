import CustomStructures.MyGraph as cg
import AIAlgorithms.treesearch as ai_alg


# ========================================== [DEFINING SPACE]

def creating_graph():

    problem_space = cg.MyGraph()
    problem_space.add_node(1, custom_attributes={'name': 'Oradea'})
    problem_space.add_node(2, custom_attributes={'name': 'Zerind'})
    problem_space.add_node(3, custom_attributes={'name': 'Arad'})
    problem_space.add_node(4, custom_attributes={'name': 'Timisoara'})
    problem_space.add_node(5, custom_attributes={'name': 'Lugoj'})
    problem_space.add_node(6, custom_attributes={'name': 'Mehadia'})
    problem_space.add_node(7, custom_attributes={'name': 'Drobeta'})
    problem_space.add_node(8, custom_attributes={'name': 'Sibiu'})
    problem_space.add_node(9, custom_attributes={'name': 'Rimnicu Vilcea'})
    problem_space.add_node(10, custom_attributes={'name': 'Craiova'})
    problem_space.add_node(11, custom_attributes={'name': 'Fagaras'})
    problem_space.add_node(12, custom_attributes={'name': 'Pitesti'})
    problem_space.add_node(13, custom_attributes={'name': 'Bucharest'})
    problem_space.add_node(14, custom_attributes={'name': 'Giurgiu'})
    problem_space.add_node(15, custom_attributes={'name': 'Neamt'})
    problem_space.add_node(16, custom_attributes={'name': 'Iasi'})
    problem_space.add_node(17, custom_attributes={'name': 'Vasliu'})
    problem_space.add_node(18, custom_attributes={'name': 'Urziceni'})
    problem_space.add_node(19, custom_attributes={'name': 'Hirsova'})
    problem_space.add_node(20, custom_attributes={'name': 'Eforie'})

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