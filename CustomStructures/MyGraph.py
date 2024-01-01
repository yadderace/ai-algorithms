import networkx as nx

class GraphNode():

    def __init__(self, node_id, custom_attributes):
        self.node_id = node_id
        self.path_cost = 0
        self.neighbor_nodes = {}
        self.custom_attributes = custom_attributes

    def add_neighbor_node(self, node_id, node):
        self.neighbor_nodes[node_id] = node


class MyGraph(nx.Graph):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_node(self, node_id, custom_attributes=None):
        node = GraphNode(node_id, custom_attributes)
        super().add_node(node_id, data=node)

    def add_edges_from(self, ebunch_to_add, **attr):
        
        for edge in ebunch_to_add:
            node_id1, node_id2 = edge
            node1 = self.nodes[node_id1]['data']
            node2 = self.nodes[node_id2]['data']
            node1.add_neighbor_node(node_id1, node1)
            node2.add_neighbor_node(node_id2, node2)

        return super().add_edges_from(ebunch_to_add, **attr)