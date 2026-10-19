# Implement merge sort in Python and test it on a random list. Use a list data
# structure implemented in Assignment 2. Measure the runtime for growing input
# sizes and compare it with the theoretical O(n log n) bound.

import random
import time
import math


def merge_sort(L):
    if len(L) <= 1:
        return L
    left, right = split(L)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def split(L):
    m = len(L) // 2
    p = L.lst
    for _ in range(m-1):
        p = p.nxt
    left = LinkedList()
    right = LinkedList()
    left.lst = L.lst
    right.lst = p.nxt
    p.nxt = None

    return left, right


def merge(L0, L1):
    result = LinkedList()
    tail = None
    p = L0.lst
    q = L1.lst
    while p is not None and q is not None:
        if p.val <= q.val:
            v = p.val
            p = p.nxt
        else:
            v = q.val
            q = q.nxt
        new = LLNode(v)
        if tail is None:          # result is still empty
            result.lst = new
        else:
            tail.nxt = new
        tail = new
    
    # one list is used up, the rest of the other one is still missing
    if p is not None:
        rest = p
    else:
        rest = q

    if tail is None:
        result.lst = rest
    else:
        tail.nxt = rest
    
    return result



# singly linked list from a2
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
                                 

class LLNode:
    def __init__(self , d):
        self.val = d
        self.nxt = None
    def __repr__(self):
        return (str(self.val) + " nxt- " + str(self.nxt))


# test it on a random list
import random

L = LinkedList()
for _ in range(10):
    L.append(random.randint(1, 100))
print(L.lst)                  # before
L = merge_sort(L)
print(L.lst)                  # after: should be sorted

# measure the run time
def build_random_list(n):
    L = LinkedList()
    tail = None
    for _ in range(n):
        new = LLNode(random.randint(1, 1000000))
        if tail is None:
            L.lst = new
        else:
            tail.nxt = new
        tail = new
    return L

print("n        time (s)    time / (n log n)")
for n in [1000, 2000, 4000, 8000, 16000, 32000]:
    L = build_random_list(n)          # not timed
    start = time.perf_counter()
    merge_sort(L)                     # only this is timed
    t = time.perf_counter() - start
    print(n, round(t, 4), round(t / (n * math.log2(n)) * 1e9, 1))