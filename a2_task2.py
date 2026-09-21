# We discussed a python implementation for linked lists. Add the missing operations
# empty, len , and delete. Check their implementation.


class LinkedList ():
    def __init__(self):
        self.lst = None  # the head of linked list
    def append(self , d):
        if self.lst is None:
            self.lst = LLNode(d)
        else:
            p = self.lst
            while p.nxt is not None:
                p = p.nxt
            p.nxt = LLNode(d)

    # empty
    def empty(self):
        if self.lst is None:
            return True
        else:
            return False

    # another way for empty:
    # return self.lst is None

    # len
    def __len__(self):
        count = 0
        p = self.lst
        while p is not None:
            count += 1
            p = p.nxt
        return count
            




class LLNode:
    def __init__(self , d):
        self.val = d
        self.nxt = None
    def __repr__(self):
        return (str(self.val) + " nxt- " + str(self.nxt))