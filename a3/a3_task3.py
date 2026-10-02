# Implement a Stack and a Queue in Python on top of the list data structure you
# already implemented. Give the runtime of every operation and explain which
# underlying representation you chose for each of the two ADTs and why.


# 1. stack
# chose singly linked list, using the head as the top. 
# All operations only touch the head, so they're O(1), and the extra prev pointer of a doubly linked list would give no benefit.


# single linked list classes from a2
class LLNode:
    def __init__(self , d):
        self.val = d
        self.nxt = None
    def __repr__(self):
        return (str(self.val) + " nxt- " + str(self.nxt))

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

    # delete
    # Deletes the first node with value d (same behavior as SimpleList.delete, slide 24).
    # If d is not in the list, the list is unchanged.
    def delete(self, d):
        if self.lst is None:
            return
        elif self.lst.val == d:
            self.lst = self.lst.nxt
        else:
            p = self.lst
            while p.nxt is not None:
                if p.nxt.val == d:
                    p.nxt = p.nxt.nxt  # skip the node we wanna delete
                    return  # after delete the value, end the function in case it crash,only delete the first node that has the value
            
                p = p.nxt


# stack class
class Stack:
    def __init__(self):
        self.items = LinkedList()
    
    def empty(self):
        return self.items.empty()
    
    def top(self):
        if self.items.empty():
            return None
        else:
            return self.items.lst.val  

    def push(self , v):
        p = self.items.lst
        self.items.lst = LLNode(v)
        self.items.lst.nxt = p

    def pop(self):
        top_value = self.top()
        self.items.delete(top_value)


# All Stack operations are O(1): they only touch the head of the list.
#   __init__  O(1)  create an empty LinkedList
#   empty     O(1)  LinkedList.empty only checks the head
#   top       O(1)  reads the head's value
#   push      O(1)  
#   pop       O(1)  


# 2. queue - still choose single linked list
# with a tail reference kept in queue
# enqueue at the tail and dequeue at the head are both O(1), and each node only
# needs one pointer, so it uses less memory than a doubly linked list.
# Runtime: __init__, enqueue, dequeue, empty, count are all O(1)
# (count uses the Queue's own size counter, since LinkedList.__len__ is O(n)).



# queue class

class queue:
    def __init__(self):
        self.items = LinkedList()
        self.tail = None   # tail pointer
        self.size = 0      # size counter

    # add the value to the back of the queue
    def enqueue(self,v):
        new_tail = LLNode(v)
        if self.items.lst is None:
            self.items.lst = new_tail
            self.tail = new_tail
        else: 
            self.tail.nxt = new_tail
            self.tail = new_tail
        self.size += 1

    # remove and return the front value of the queue
    def dequeue(self):
        if self.items.empty():
            return None

        front_value = self.items.lst.val
        self.items.delete(front_value)

        if self.items.empty():
            self.tail = None

        self.size -= 1

        return front_value
     

    def empty(self):
        return self.items.empty()

    def count(self):
        return self.size





    
        
