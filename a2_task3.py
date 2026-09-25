

# Provide a python implementation of double linked lists.
#
# The List ADT
#
# Domain: a finite, ordered sequence L = < a_0, ..., a_(N-1) >
#         Positions are 0-based. An empty list has length 0.
#
# Syntax:
#   __init__()        ->  LIST          new empty list
#   empty()           ->  BOOLEAN
#   count()           ->  INT
#   append(x)         ->  None          add x at the end
#   add_value(p, x)   ->  None          insert x at position p   (slide 14)
#   remove(p)         ->  None          remove element at p      (slide 15)
#   search(x)         ->  INT           position of x, -1 if not found (slide 16)
#   Return(p)         ->  value at p                             (slide 16)
#   delete(x)         ->  None          remove the first element with value x;
#                                       the list is unchanged if x is not in the list
#
# Semantics:
#   empty(new list)                 = True
#   count(new list)                 = 0
#   add_value(p, x) with 0 <= p <= N inserts x, so Return(p) = x
#   remove(p) with 0 <= p < N removes a_p
#   search(x) = p if a_p = x, otherwise -1
#   "otherwise undefined" is implemented as raise IndexError
#
# Implementation notes:
#   Double linked list with references to both ends (head, tail) and a size
#   counter, so append and count run in O(1).


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
    


          




    


    






                     



        

