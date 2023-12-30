import networkx as nx

class GraphNode():

    def __init__(self, node_id, other_attributes):
        self.node_id = node_id
        self.other_attributes = other_attributes


class MyGraph(nx.Graph):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_my_node(self, node_id, custom_attributes=None):
        node = GraphNode(node_id, custom_attributes)
        self.add_node(node_id, data=node)