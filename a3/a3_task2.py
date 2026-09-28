# Implement a binary tree in Python and provide pre-order, in-order, post-order
# and level-order traversals. Give the runtime of each traversal and explain which
# additional data structure the level-order traversal needs.

from collections import deque


class BTree:  # actually is the node, since the whole tree is just root node so we only need this one class
    def __init__(self):
        self.key = None
        self.parent = None
        self.left = None
        self.right = None


def preorder_traverse(u):
    if u is None:
        return
    print(u.key,end=" ")
    preorder_traverse(u.left)
    preorder_traverse(u.right)


def inorder_traverse(u):
    if u is None:
        return
    inorder_traverse(u.left)
    print(u.key, end=" ")
    inorder_traverse(u.right)


def postorder_traverse(u):
    if u is None:
        return
    postorder_traverse(u.left)
    postorder_traverse(u.right)
    print(u.key, end=" ")

# to do this, we need queue here
def levelorder_traverse(u):
    if u is None:
        return
    q = deque() # create a new queue
    q.append(u)
    while len(q) > 0:
        u = q.popleft()  # take the top node
        print(u.key, end=" ")
        if u.left is not None:
            q.append(u.left) # put the child at the end of the queue
        if u.right is not None:
            q.append(u.right)



# Runtime:
# preorder, inorder, postorder: O(n). Each node causes exactly one call,
#   plus n+1 calls on empty children (None), so 2n+1 calls in total,
#   each doing O(1) work.
# levelorder: O(n). Each node is enqueued once and dequeued once,
#   and deque.append / deque.popleft are both O(1).
#
# Additional data structure for levelorder: a queue (FIFO).
# Children are added at the back, so all nodes of one level are
# dequeued before any node of the next level. A stack (LIFO) would
# go deep first instead of level by level.


