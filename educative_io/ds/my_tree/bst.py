
from ds_tree import BinaryTreeNode


class BST:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
    
    def insert(self, data):
        node = BinaryTreeNode(data)

        if self.root is None:
            self.root = node
        else:
            self.insert_helper(self.root, node)
        

    def insert_helper(self, current_node: BinaryTreeNode, new_node: BinaryTreeNode):

        if current_node.value < new_node.value:
            if current_node.rightNode:
                self.insert_helper(current_node.rightNode, new_node)
            else:
                current_node.rightNode = new_node
        else:
            if current_node.leftNode:
                self.insert_helper(current_node.leftNode, new_node)
            else:
                current_node.leftNode = new_node

    def contains(self, node_value):
        return self.contains_helper(self.root, node_value)

    def contains_helper(self, node: BinaryTreeNode, node_value):
        
        if node is None:
            return False
        elif node.value == node_value:
            return True
        elif node.value < node_value:
            return self.contains_helper(node.rightNode, node_value)
        else:
             return self.contains_helper(node.leftNode, node_value)

    def is_valid_bst(self):
        return self.validate_left(self.root.leftNode, self.root.value) and self.validate_right(self.root.rightNode, self.root.value) 

    def validate_left(self, node: BinaryTreeNode, root_value):
         
        if node is None:
            return True
        
        if node.value > root_value:
            return False
        else:
            return self.validate_left(node.leftNode, root_value) and self.validate_left(node.rightNode, root_value)
    
    def validate_right(self, node: BinaryTreeNode, root_value):
        
        if node is None:
                return True

        if node.value < root_value:
            return False
        else:
            return self.validate_left(node.leftNode, root_value) and self.validate_left(node.rightNode, root_value)
