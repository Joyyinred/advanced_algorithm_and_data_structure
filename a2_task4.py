# Write a method, reverse(), that reverses the order of elements in a Double Linked class Node:
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

    def reverse(self):
        old_head = self.head
        old_tail = self.tail
        p = self.head
        
        while p is not None:
            before = p.prev
            after = p.next
            if before is None:
                p.next = None
                p.prev = after

            elif after is None:
                p.prev = None
                p.next = before

            else:
                p.next = before
                p.prev = after

            p = after  # move to next one, use after instead of p.prev since the value of it is already changed

        self.head = old_tail
        self.tail = old_head
                


