from my_tree.tree import BinaryTree
from my_tree.tree import BinaryTreeNode
from my_queue.my_queue import MyQueue

q = MyQueue()

def traversal(rootNode: BinaryTreeNode):
    q.enqueue(rootNode)
    my_str = level_order_tree_traversal(rootNode)
    print(my_str)


def level_order_tree_traversal(node: BinaryTreeNode):
    my_str = ""
    if node:
        my_str += str(node.value)
        q.dequeue()
        q.enqueue(node.leftNode)
        q.enqueue(node.rightNode)
        my_str +=  level_order_tree_traversal(q.peek())
    return my_str



root = BinaryTreeNode(1)
root.leftNode = BinaryTreeNode(2)
root.leftNode.leftNode = BinaryTreeNode(4)
root.leftNode.rightNode = BinaryTreeNode(5)
root.rightNode = BinaryTreeNode(3)
root.rightNode.leftNode = BinaryTreeNode(6)
root.rightNode.rightNode = BinaryTreeNode(7)

b = BinaryTree(root)
traversal(root)