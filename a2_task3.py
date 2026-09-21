# Provide a python implementation of double linked lists. 
# operations: append,insert, empty,len,delete,Search
# append → prepend → insert (which uses both) → delete


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

    # insert
    def insert(self,index,d):

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

    # empty
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def __len__(self):
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
    


          




    


    






                     



        

