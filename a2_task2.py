# We discussed a python implementation for linked lists. Add the missing operations
# empty, len , and delete. Check their implementation.


class LinkedList ():
    def __init__(self):
        self.lst = None
    def append(self , d):
        if self.lst is None:
            self.lst = LLNode(d)
        else:
            p = self.lst
            while p.nxt is not None:
                p = p.nxt
            p.nxt = LLNode(d)

class LLNode:
    def __init__(self , d):
        self.val = d
        self.nxt = None
    def __repr__(self):
        return (str(self.val) + " nxt- " + str(self.nxt))