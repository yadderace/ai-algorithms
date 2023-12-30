import CustomStructures.MyGraph as cg

from AIAlgorithms.treesearch import simple_treesearch


# ========================================== [DEFINING SPACE]
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
problem_space.add_edges_from([(2,3)])
problem_space.add_edges_from([(3,4), (3,8)])
problem_space.add_edges_from([(4,5)])
problem_space.add_edges_from([(5,6)])
problem_space.add_edges_from([(6,7)])
problem_space.add_edges_from([(7,10)])
problem_space.add_edges_from([(8,9), (8,11)])
problem_space.add_edges_from([(9,10), (9, 12)])
problem_space.add_edges_from([(10,12)])
problem_space.add_edges_from([(11,13)])
problem_space.add_edges_from([(12,13)])
problem_space.add_edges_from([(13,14), (13,18)])
problem_space.add_edges_from([(15,16)])
problem_space.add_edges_from([(16,17)])
problem_space.add_edges_from([(17,18)])
problem_space.add_edges_from([(18,19)])
problem_space.add_edges_from([(19,20)])

# ========================================== [SIMPLE TREE SEARCH]
problem1 = {
    'init_state_id': 3,
    'end_state_id': 12
}
solution = simple_treesearch(problem=problem1, space=problem_space)
print(solution)