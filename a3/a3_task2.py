# Implement a binary tree in Python and provide pre-order, in-order, post-order
# and level-order traversals. Give the runtime of each traversal and explain which
# additional data structure the level-order traversal needs.

from collections import deque

# Binary search tree ADT
# A binary tree where every node has at most two children. In a binary
# search tree the keys are ordered: left subtree < key < right subtree.
# add, find and remove keep this order. The traversals work on any binary tree.
#
# Design (two classes):
#   BTree             the node class (key, parent, left, right);
#                     does the recursive work
#   BinarySearchTree  the tree; holds the root (None = empty tree), so an
#                     empty tree and removing the last node are supported
#
# Syntax (BinarySearchTree, the operations a user calls):
#   BinarySearchTree()      -> TREE      new empty tree
#   empty()                 -> BOOLEAN
#   size()                  -> INT       number of nodes, 0 if empty
#   height()                -> INT       longest path to a leaf, leaf = 0, empty = -1
#   find(x)                 -> key | None
#   add(x)                  -> BOOLEAN   False if x already exists
#   remove(x)               -> BOOLEAN   False if x is not in the tree
#   preorder_traverse()     -> None      prints keys: node, left, right
#   inorder_traverse()      -> None      prints keys: left, node, right
#   postorder_traverse()    -> None      prints keys: left, right, node
#   levelorder_traverse()   -> None      prints keys level by level (uses a queue)
#
# Node operations (BTree):
#   depth()                 -> INT       number of edges to the root
#   remove_node(u)          -> BOOLEAN   remove node u from the tree
#   helpers used by add/remove: find_last, add_child, splice

# Semantics:
#   empty(new tree)   = True
#   size(new tree)    = 0
#   height(new tree)  = -1
#   find(x)           = x if x is in the tree, otherwise None
#
#   add(x), x not in the tree:  returns True,  find(x) = x,  size increases by 1
#   add(x), x already in tree:  returns False, tree unchanged
#   remove(x), x in the tree:   returns True,  find(x) = None, size decreases by 1
#   remove(x), x not in tree:   returns False, tree unchanged
#
#   size(u)   = 1 + size(u.left) + size(u.right),         empty subtree = 0
#   height(u) = 1 + max(height(u.left), height(u.right)), empty subtree = -1
#   depth(root) = 0,  depth(u) = depth(u.parent) + 1
#
#   After every add and remove: left subtree < key < right subtree,
#   so inorder_traverse prints the keys in sorted order.
#   Every traversal prints each key exactly once.


class BTree:  # the node class; the whole tree is the BinarySearchTree below
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
        return d

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
        return self.add_child(p,u)
        

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
        # find u's only child s, can be none if its just a leaf
        if u.left is not None:
            s = u.left 
        else:
            s = u.right

        # if u is the root node
        if u.parent is None:
            if s is None:
                return False
            u.key = s.key
            u.left = s.left
            u.right = s.right

            if u.left is not None:
                u.left.parent = u
            if u.right is not None:
                u.right.parent = u
            return True
            
        # u is not root, let the parent has s as child
        p = u.parent
        if p.left == u:
            p.left = s
        else:
            p.right = s
        if s is not None:
            s.parent = p

        return True

    def remove_node(self,u):
        if u.left is None or u.right is None:
            return self.splice(u)
        else:
            w = u.right
            while w.left is not None:
                w = w.left
            u.key = w.key
            return self.splice(w)

    # delete the value
    def remove(self, x):
        u = self.find_last(x)
        if u.key != x:          # didnt find x
            return False
        return self.remove_node(u)



    def preorder_traverse(self):
        print(self.key,end=" ")
        if self.left is not None:
            self.left.preorder_traverse()
        if self.right is not None:
            self.right.preorder_traverse()


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

class BinarySearchTree:
    
    # tree object only holds the root (none = empty tree)
    # all the recursive work is done by the BTree nodes
    
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root is None

    def size(self):
        if self.root is None:
            return 0
        return self.root.size()

    def height(self):
        if self.root is None:
            return -1                  
        return self.root.height()

    def find(self, x):
        if self.root is None:
            return None
        return self.root.find(x)

    def add(self, x):
        if self.root is None:          # empty tree: the new node becomes the root
            self.root = BTree()
            self.root.key = x
            return True
        return self.root.add(x)

    def remove(self, x):
        if self.root is None:          # empty tree: nothing to remove
            return False
        # the root is the only node and has key x: the tree becomes empty
        if self.root.left is None and self.root.right is None and self.root.key == x:
            self.root = None
            return True
        return self.root.remove(x)

    def preorder_traverse(self):
        if self.root is not None:
            self.root.preorder_traverse()
        print()

    def inorder_traverse(self):
        if self.root is not None:
            self.root.inorder_traverse()
        print()

    def postorder_traverse(self):
        if self.root is not None:
            self.root.postorder_traverse()
        print()

    def levelorder_traverse(self):
        if self.root is not None:
            self.root.levelorder_traverse()
        print()



# Runtime:
# preorder, inorder, postorder: O(n). 
# Each node is visited by exactly one call (children are checked for None before calling, so there are no
# calls on empty subtrees), and each call does O(1) work.
# levelorder: O(n). Each node is enqueued once and dequeued once,
# and deque.append / deque.popleft are both O(1).
#
# Additional data structure for levelorder: a queue (FIFO).
# Children are added at the back, so all nodes of one level are
# dequeued before any node of the next level. A stack (LIFO) would
# go deep first instead of level by level.


