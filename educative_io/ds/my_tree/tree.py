class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def traversal(self, traversal_type):
        traversal = ""
        if traversal_type == "in-order":
            traversal = self.in_order_traversal(self.root)
        elif traversal_type == "pre-order":
            traversal = self.pre_order_traversal(self.root)
        elif traversal_type == "post-order":
            traversal = self.post_order_traversal(self.root)
        print(traversal)
    
    def in_order_traversal(self, node):
        traversal = ""
        if node is None:
            return traversal
        traversal += self.in_order_traversal(node.leftNode)
        traversal += str(node.value) + "-"
        traversal += self.in_order_traversal(node.rightNode)
        return traversal

    def pre_order_traversal(self, node):
        traversal = ""
        if node is None:
            return traversal
        traversal += str(node.value) + "-"
        traversal += self.pre_order_traversal(node.leftNode)
        traversal += self.pre_order_traversal(node.rightNode)
        return traversal

    def post_order_traversal(self, node):
        traversal = ""
        if node is None:
            return traversal
        traversal += self.post_order_traversal(node.leftNode)
        traversal += self.post_order_traversal(node.rightNode)
        traversal += str(node.value) + "-"
        return traversal
