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
#   push      O(1)  LinkedList.prepend, no loop
#   pop       O(1)  LinkedList.pop_front, no loop


# 2. queue - choose doubly linked list
# Why a doubly linked list?
# A queue is FIFO: elements are added at one end (the back) and removed at the
# other end (the front). So, unlike the stack, the queue needs fast access to
# BOTH ends of the list.
#
# - Our doubly linked list keeps a reference to the head AND the tail, so
#     enqueue = append(v)          -> jumps directly to the tail, O(1)
#     dequeue = Return(0), remove(0) -> only touches the head,   O(1)


# doubly link list class from a2
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # append
    def append(self, d):
        new = Node(d)
        # when the list is empty
        if self.head is None:
            self.head = new
            self.tail = new

        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self.size += 1

    # insert(add_value)
    def add_value(self,index,d):

        # check index validation
        if index < 0 or index > self.size:
            raise IndexError("index out of range")


        new = Node(d)
        # empty list
        if self.head is None:
            self.head = new
            self.tail = new

        elif index == 0:
            old_head = self.head
            self.head = new
            self.head.next = old_head
            old_head.prev = new
            

        elif index == self.size:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

        
        else:
            # find p, which is the node before that index location we want to insert
            p = self.head
            for _ in range (index-1):
                p = p.next
            # create variables to save the value before and after the new value 
            before = p
            after = p.next

            # create link
            before.next = new
            new.prev = p

            new.next = after
            after.prev = new

        self.size += 1

    # delete
    def delete(self,d):
        if self.head is None:
            return
        else:
            p = self.head
            while p is not None:
                if p.data == d:
                    before = p.prev
                    after = p.next

                    if before is None:  # if the value is head
                        self.head = p.next
                    else:
                        before.next = after

                    if after is None:   # if the value is tail
                        self.tail = self.tail.prev
                    else:
                        after.prev = before


                    self.size -= 1

                    return
                
                p = p.next

    # remove: takes an index and removes the node at that position
    def remove(self, index):
        # check index validation
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")

        # walk to the node at position index
        p = self.head
        for _ in range(index):
            p = p.next

        before = p.prev
        after = p.next

        if before is None:      # the node is the head
            self.head = after
        else:
            before.next = after

        if after is None:       # the node is the tail
            self.tail = before
        else:
            after.prev = before

        self.size -= 1

    # empty
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def count(self):
        return self.size

    # search：takes the value and returns an index
    def search(self,d):
        if self.head is None:
            return -1
        else:
            p = self.head
            index = 0
            while p is not None:
                if p.data == d:
                    return index
                # if not match we continue check the next one, until its matching and returning the index
                p = p.next
                index += 1

            return -1

    # return: it takes an index and returns a value.
    def Return(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")

        else:
            p = self.head
            
            for _ in range(index):
                p = p.next

            return p.data

    # print
    def print_forward(self):
        p = self.head
        while p is not None:
            print(p.data,end=" ")
            p = p.next
        print()

    def print_backward(self):
        p = self.tail
        while p is not None:
            print(p.data,end=" ")
            p = p.prev
        print()

# queue class
# Runtime of every operation:
#   __init__  O(1)
#   enqueue   O(1)
#   dequeue   O(1)
#   empty     O(1)  (uses the size counter)
#   count     O(1)  (uses the size counter)

class queue:
    def __init__(self):
        self.items = double_linked_list()

    # push the value to the back of the queue
    def enqueue(self,v):
        self.items.append(v)

    # remove and return the front value of the queue
    def dequeue(self):
        if self.items.empty():
            return None
        front_value = self.items.Return(0)
        self.items.remove(0)

        return front_value

    def empty(self):
        return self.items.empty()

    def count(self):
        return self.items.count()

    
        
