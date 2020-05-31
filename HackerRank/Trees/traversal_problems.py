import sys
sys.path.append("..") # to import higher directory.
from Queues.queue import Queue

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):

        if traversal_type == "preorder":
            return self.preorder_print(tree.root)
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root)
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root)
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " not recognized.")
            return False

    def preorder_print(self, start):
        """Root->Left-Right"""
        if start is None:
            return 
        print(str(start.value)+ " ", end="")
        self.preorder_print(start.left)
        self.preorder_print(start.right)

    def inorder_print(self, start):
        """Left->Root->Right"""
        if start is None:
            return
        self.inorder_print(start.left)
        print(str(start.value)+ " ", end="")
        self.inorder_print(start.right)

    def postorder_print(self, start):
        """Left->Right->Root"""
        if start is None:
            return
        self.postorder_print(start.left)
        self.postorder_print(start.right)
        print(str(start.value)+ " ",end="")

    def height(self, node):
        """As height of leaf nodes is 0 so -1 + 1 = 0"""
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def levelorder_print(self, start):
        """Level by level and left to right using queues"""
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)

        while len(queue) > 0:
            print(str(queue.peek())+ " ",end="")
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.print_tree("levelorder")

