class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedlist():
	def __init__(self):
		self.head = None

	def append(self,data):
		new_node = Node(data)
		cur_node = self.head

		if self.head is None:
			self.head = new_node
			return

		while cur_node.next:
			cur_node = cur_node.next
		cur_node.next = new_node

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next

	def prepend(self,data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self,prev_node,data):
		new_node = Node(data)

		if not prev_node:
			print("Previous node not present in linkedlist")
			return

		new_node.next = prev_node.next
		prev_node.next = new_node

	def reverse(self):

		prev = None
		cur = self.head
		while cur:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		self.head = prev


ll = linkedlist()
ll.append("A")
ll.append("B")
ll.append("C")
ll.reverse()
ll.print_list()



