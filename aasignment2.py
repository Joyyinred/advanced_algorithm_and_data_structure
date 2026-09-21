# 1. For double linked lists implement a method rotate(r) that rotates the list so that
# list item i becomes list item (i + r) mod n, ∀i ∈ {0, ..., n} where n is the length
# of the list. What is the runtime?

# before the function, we have to implement a double linked list class and its node
# i is the index of the node in the list, r is the parameter to show how many positions/steps this node will move, 
# and (i+r) mod n is the new index of the item we moved

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


    def rotate(self,r):
        # when the size of list is 0 or 1
        if self.size < 2:
            return 
        # since r can be a big number but actually it just moves within the length of list,so we better normalize it
        r = r % self.size

        # rotating by a multiple of n changes nothing
        if r == 0:   
            return

        # then we need to find the new head of the list, we walk to the node that will be the new head (old_index = n - r)
        # and here we dont rotate the list yet, just move the pointer to the new head
        current = self.head
        for _ in range (self.size - r):
            current = current.next

        # now we let the node we found to be the new head
        # before changing node, we save them first
        
        new_tail = current.prev  # the node before new head become new tail
        old_head = self.head
        old_tail = self.tail

        # create link between old head and old tail since now they are no longer head and tail, 
        # and supposed to be node inside of list
        old_tail.next = old_head
        old_head.prev = old_tail
        # get the node for new tail and head
        new_tail.next = None
        current.prev = None
        # get new head and tail
        self.head = current
        self.tail = new_tail




