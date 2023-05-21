class Node:
	def __init__(self, key = None, left = None, right = None, parent = None):
		self.left = left
		self.right = right
		self.key = key
		self.parent = parent

	@staticmethod
	def min(*arg):
		minNode = None
		minWeight = 1e99
		for node in arg:
			if node is None:
				continue

			if not isinstance(node, Node):
				raise ValueError("Invalid data type for comparison")

			if node.key < minWeight:
				minNode = node
				minWeight = node.key

		#print(minNode, minWeight)
		return minNode

def findInOrderSuccessorGivenRoot(root, node):
	if root is None:
		return None

	if root.key > node.key:
		return Node.min(root, findInOrderSuccessorGivenRoot(root.left, node), findInOrderSuccessorGivenRoot(root.right, node))

	return Node.min(findInOrderSuccessorGivenRoot(root.left, node), findInOrderSuccessorGivenRoot(root.right, node))

def findInOrderSuccessor(node):
	if node is None:
		return None

	if node.right is not None:
		right_side = node.right

		while right_side is not None and right_side.left is not None and right_side.key > node.key:
			right_side = right_side.left

		return right_side


	parent_side = node
	parent_dummy = node

	while parent_side is not None:
		parent_dummy = parent_side
		parent_side = parent_side.parent

		if parent_side.key > parent_dummy.key:
			return parent_side

	return None

if __name__ == '__main__':
	l1 = Node(11)
	l2 = Node(14)

	n1 = Node(12, l1, l2)
	l3 = Node(5)
	n2 = Node(9, l3, n1)
	l4 = Node(25)
	root = Node(20, n2, l4)

	l1.parent = n1
	l2.parent = n1
	n1.parent = n2
	l3.parent = n2
	n2.parent = root
	l4.parent = root
	root.parent = None

	print(findInOrderSuccessor(n2).key)