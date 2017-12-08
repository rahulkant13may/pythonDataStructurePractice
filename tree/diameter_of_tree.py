class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def height(node):
	if node is None:
		return 0

	return 1 + max(height(node.left), height(node.right))

def diameterTree(root):

	if root is None:
		return 0

	leftHeight = height(root.left)
	rightHeight = height(root.right)

	leftDiameter = diameterTree(root.left)
	rightDiameter = diameterTree(root.right)

	return max(leftHeight + rightHeight + 1, max(leftDiameter, rightDiameter))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)
print("Diameter of given binary tree is %d" %(diameterTree(root)))