
class ListNode:
	def __init__(self, val = None, next = None):
		self.val = val
		self.next = next

	def __str__(self):
		return str(self.val)

class Queue:
	def __init__(self):
		self.end = None
		self.head = self.end


	def pop(self):
		res = self.head
		
		if res is None:
			raise ValueError("Cannot pop from empty queue")
		
		self.head = self.head.next
		return res
	
	def push(self, val):
		if self.head is None:
			self.end = ListNode(val)
			self.head = self.end
		else:
			self.end.next = ListNode(val)
			self.end = self.end.next

	def __str__(self):
		dummy = self.head
		res = []
		while dummy:
			res.append(str(dummy.val))
			dummy = dummy.next
		x = f'[{",".join(res)}]'
		return x
