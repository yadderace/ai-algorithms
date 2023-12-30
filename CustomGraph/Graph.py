import networkx as nx

from CustomGraph.GraphNode import GraphNode

class CustomGraph(nx.Graph):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_my_node(self, node_id, custom_attributes=None):
        node = GraphNode(node_id, custom_attributes)
        self.add_node(node_id, data=node)