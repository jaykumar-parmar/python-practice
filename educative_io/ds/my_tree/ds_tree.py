import numbers
import math

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

    def size(self, node):

        if node is None:
            return 0
        return self.size(node.leftNode) + self.size(node.rightNode) + 1

    def size_iterative(self):
        node_stack = []
        node = self.root
        node_stack.append(node)
        cnt = 0

        while len(node_stack):
            node = node_stack.pop()
            cnt += 1

            if(node.rightNode):
                node_stack.append(node.rightNode)
            
            if node.leftNode:
                node_stack.append(node.leftNode)
        return cnt


    def height(self):
        node_count = self.node_count()
        return math.log((node_count + 1), 2)
