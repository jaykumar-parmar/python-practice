from tree import BinaryTree, BinaryTreeNode
   
root = BinaryTreeNode(1)
root.leftNode = BinaryTreeNode(2)
root.leftNode.leftNode = BinaryTreeNode(4)
root.leftNode.rightNode = BinaryTreeNode(5)
root.rightNode = BinaryTreeNode(3)
root.rightNode.leftNode = BinaryTreeNode(6)
root.rightNode.rightNode = BinaryTreeNode(7)

b = BinaryTree(root)
b.traversal("pre-order")
b.traversal("in-order")
b.traversal("post-order")