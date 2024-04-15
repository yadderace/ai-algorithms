from treelib import Node, Tree


class MyTreeNode(Node):
    def __init__(self, tag, identifier=None, node_id = None, data=None, tree=None, utility=0):
        super().__init__(tag=tag, identifier=identifier, data=data)
        self.node_id = node_id
        self.utility = utility
        self.tree = tree

    def get_child_node(self, node_id):
        childs = self.tree.children(self.identifier)
        
        for node in childs:
            if node.node_id == node_id:
                return node
        return None


class MyTree(Tree):
    def __init__(self, tree_id=None):
        super().__init__(tree_id)
        # Add custom attributes or methods as needed
        self.added_nodes = 0

    def create_node(self, tag, node_id = None, parent=None, data=None, utility=0):
        node = MyTreeNode(tag=tag, identifier=self.added_nodes, node_id = node_id, data=data, tree=self, utility=utility)
        self.add_node(node, parent)
        self.added_nodes += 1
        return node

    @property
    def nodes_quantity(self):
        return self.added_nodes

    @nodes.setter
    def nodes(self, new_value):
        self.added_nodes = new_value