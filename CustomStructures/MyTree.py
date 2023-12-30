from treelib import Node, Tree


class MyTreeNode(Node):
    def __init__(self, tag, identifier=None, data=None, expanded=True, parent=None):
        super().__init__(tag, identifier, data, expanded, parent)

class MyTree(Tree):
    def __init__(self, tree_id=None):
        super().__init__(tree_id)
        # Add custom attributes or methods as needed

    def create_node(self, tag, identifier=None, parent=None, data=None):
        node = MyTreeNode(tag, identifier, data, parent=parent)
        self.add_node(node, parent)
        return node