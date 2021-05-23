

from platform import node
from string import printable
from educative_io.ds.my_tree.tree import BinaryTree, BinaryTreeNode


my_stack = []
def reverse_level_order_traversal(rootnode: BinaryTreeNode):
    my_stack.append(rootnode.value)
    reverse_node_traversal(rootnode)
    
    print(my_stack)

    while len(my_stack) > 0:
        print(my_stack.pop())


def reverse_node_traversal(rootnode: BinaryTreeNode):
    if rootnode is None:
        return

    if rootnode.leftNode:
        my_stack.append(rootnode.leftNode.value)
    
    if rootnode.rightNode:
        my_stack.append(rootnode.rightNode.value)
    
    reverse_node_traversal(rootnode.leftNode)
    reverse_node_traversal(rootnode.rightNode)


root = BinaryTreeNode(1)
root.leftNode = BinaryTreeNode(2)
root.leftNode.leftNode = BinaryTreeNode(4)
root.leftNode.leftNode.leftNode = BinaryTreeNode(8)
root.leftNode.leftNode.rightNode = BinaryTreeNode(9)

root.leftNode.rightNode = BinaryTreeNode(5)

root.rightNode = BinaryTreeNode(3)
root.rightNode.leftNode = BinaryTreeNode(6)
root.rightNode.rightNode = BinaryTreeNode(7)

b = BinaryTree(root)
# reverse_level_order_traversal(root)
print(b.size_iterative())
