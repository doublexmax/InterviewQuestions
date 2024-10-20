from collections import deque
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

l1 = Node(12)
l2 = Node(7)
l3 = Node(1)
l4 = Node(14)

n2 = Node(4, left = l1, right = l2)
n3 = Node(6, left = l3, right = l4)
root = Node(8, left = n2, right = None)

queue = deque([(root, 0)])
added_element_from_even = False

res = []

while queue:
    #print(queue)

    node, level = queue.popleft()
    if node is None:
        continue
    if level & 1 == 1:
        added_element_from_even = False
        if not queue or queue[0][1] != level:
            res.append(node.val)
    elif not added_element_from_even:
        res.append(node.val)
        added_element_from_even = True

    if node.left:
        queue.append((node.left, level + 1))
    if node.right:
        queue.append((node.right, level + 1))

print(res)
