from treelib import Node, Tree


class MyTreeNode(Node):
    def __init__(self, tag, identifier=None, node_id = None, data=None, tree=None, g_cost = 0, h_cost=0):
        super().__init__(tag=tag, identifier=identifier, data=data)
        self.node_id = node_id
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.estimated_cost = 0
        self.tree = tree
    
    def add_child(self, child_node):
        if(self.tree is not None):
            self.tree.add_node(child_node, parent = self.identifier)
            self.tree.nodes += 1



class MyTree(Tree):
    def __init__(self, tree_id=None):
        super().__init__(tree_id)
        # Add custom attributes or methods as needed
        self.tree_nodes = 0

    def create_node(self, tag, identifier=None, node_id = None, parent=None, data=None, g_cost=0, h_cost=0):
        node = MyTreeNode(tag=tag, identifier=identifier, node_id = node_id, data=data, g_cost=g_cost, h_cost=h_cost, tree=self)
        self.add_node(node, parent)
        self.nodes += 1
        return node

    @property
    def nodes(self):
        return self.tree_nodes

    @nodes.setter
    def nodes(self, new_value):
        self.tree_nodes = new_value