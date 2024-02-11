from treelib import Node, Tree


class MyTreeNode(Node):
    def __init__(self, tag, identifier=None, node_id = None, data=None, tree=None, g_cost = 0, h_cost=0):
        super().__init__(tag=tag, identifier=identifier, data=data)
        self.node_id = node_id
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.tree = tree
    
    # def add_child(self, tag, node_id = None, data=None, g_cost=0, h_cost=0):
    #     if(self.tree is not None):
    #         child_node = MyTreeNode(tag=tag, identifier=self.tree.nodes, node_id = node_id, data=data, g_cost=g_cost, h_cost=h_cost, tree=self.tree)
    #         self.tree.add_node(child_node, parent = self.identifier)
    #         self.tree.nodes += 1

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

    def create_node(self, tag, node_id = None, parent=None, data=None, g_cost=0, h_cost=0):
        node = MyTreeNode(tag=tag, identifier=self.added_nodes, node_id = node_id, data=data, g_cost=g_cost, h_cost=h_cost, tree=self)
        self.add_node(node, parent)
        self.added_nodes += 1
        return node

    @property
    def nodes(self):
        return self.added_nodes

    @nodes.setter
    def nodes(self, new_value):
        self.added_nodes = new_value