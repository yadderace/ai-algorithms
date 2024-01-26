from treelib import Node, Tree


class MyTreeNode(Node):
    def __init__(self, tag, identifier=None, data=None, g_cost = 0, h_cost=0):
        super().__init__(tag=tag, identifier=identifier, data=data)
        self.node_id = identifier
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
    
    def add_child(self, child_node):
        self.tree.add_node(child_node, parent = self.identifier)

class MyTree(Tree):
    def __init__(self, tree_id=None):
        super().__init__(tree_id)
        # Add custom attributes or methods as needed

    def create_node(self, tag, identifier=None, parent=None, data=None, g_cost=0, h_cost=0):
        node = MyTreeNode(tag=tag, identifier=identifier, data=data, g_cost=g_cost, h_cost=h_cost)
        self.add_node(node, parent)
        return node