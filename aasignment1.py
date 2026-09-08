# 1. For double linked lists implement a method rotate(r) that rotates the list so that
# list item i becomes list item (i + r) mod n, ∀i ∈ {0, ..., n} where n is the length
# of the list. What is the runtime?

# create a double linked lists
# i is the index of the node in the list, r is the parameter to show how many positions/steps this node will move

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class double_linked_list:


    def rotate(r):
        for i in range (n):
            double_linked_list[i] = double_linked_list[(i+r) % n]
