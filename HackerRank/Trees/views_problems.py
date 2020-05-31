import sys
sys.path.append("..") # to import higher directory.
from Queues.queue import Queue


class Node(object):
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def top_view(self, root):
        if root is None:
            return

        # make an empty queue for BFS
        que = Queue()

        # empty set
        sets = set(dict())

        # list to store top view keys
        topview = list()

        # append root in the queue with horizontal distance as 0
        que.enqueue((root, 0))

        while que:
            # get the element and horizontal distance
            # will use popleft() if using deque.
            node, hd = que.dequeue()

            # if the hd is seen first time it will be top view
            if hd not in sets:
                topview.append((node.info, hd))
                sets.add(hd)

            # add left and right child in the queue with hd - 1 and hd + 1
            if node.left is not None:
                que.enqueue((node.left, hd - 1))
            if node.right is not None:
                que.enqueue((node.right, hd + 1))

        for i in topview:
            print(i[0], end=' ')

    
    def bottom_view(self, root):
        if root is None:
            return

        # make an empty queue for BFS
        que = Queue()

        # dict to store bottom view keys
        # not set as for bottom view we are
        # updating/replacing the values at same horizonatal distance
        bottomview = dict()

        # append root in the queue with horizontal distance as 0
        que.enqueue((root, 0))

        while que:
            # get the element and horizontal distance
            node, hd = que.dequeue()

            # update the last seen hd element
            bottomview[hd] = node.info

            # add left and right child in the queue with hd - 1 and hd + 1
            if node.left is not None:
                que.enqueue((node.left, hd - 1))
            if node.right is not None:
                que.enqueue((node.right, hd + 1))

        for i in bottomview:
            print(bottomview[i], end=' ')


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.top_view(tree.root)
tree.bottom_view(tree.root)