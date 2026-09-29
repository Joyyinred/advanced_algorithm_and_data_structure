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

    def depth(self):
        d = 0
        u = self.parent
        while u is not None:
            u = u.parent
            d += 1
        return 

    def size(self):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size()

        right_size = 0
        if self.right is not None:
            right_size = self.right.size()

        return 1 + left_size + right_size

    def height(self):
        left_h = -1
        if self.left is not None:
            left_h = self.left.height()
        
        right_h = -1
        if self.right is not None:
            right_h = self.right.height()

        return 1 + max(left_h, right_h)

    def find(self,x):
        w = self  # root node we want to check
        while w is not None:
            if x < w.key:
                w = w.left # so we move to next node
            elif x > w.key:
                w = w.right
            else:
                return w.key
        return None

    # to do add x, we need search x, if not in the tree
    # we store x at a leaf child of the last node, p, encountered during the search
    def add(self, x):
        p = self.find_last(x)
        u = BTree()
        u.key = x
        return self.add_child(p,x)
        

    def find_last(self,x):
        w = self
        prev = None
        while w is not None:
            prev = w
            if x < w.key:
                w = w.left
            elif x > w.key:
                w = w.right
            else:
                return w
        return prev

    def add_child(self,p,u):
        if p is None:
            return False
        else:
            if u.key < p.key:
                p.left = u
                u.parent = p
            elif u.key > p.key:
                p.right = u
                u.parent = p
            else:
                return False
        return True

    def splice(self,u):
        if u.left is not None:
            s = u.left
        else:
            s = u.right
        if u == self:
            self = s
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s is not None:
            s.parent = p




    





    def preorder_traverse(self):
        print(self.key,end=" ")
        if self.left is not None:
            self.left.preorder_traverse()
        if self.right is not None:
            self.left.preorder_traverse()


    def inorder_traverse(self):
        if self.left is not None:
            self.left.inorder_traverse()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.inorder_traverse()


    def postorder_traverse(self):
        if self.left is not None:
            self.left.postorder_traverse()
        if self.right is not None:
            self.right.postorder_traverse()
        print(self.key, end=" ")

    # to do this, we need queue here
    def levelorder_traverse(self):
        q = deque() # create a new queue
        q.append(self)
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


