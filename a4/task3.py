# Implement a function BFS(G,v,...) that searches for a node u in a graph G using
# breadth first search and additionally returns the number of edges on the shortest
# path from v to u. Provide an example to test this function and explain why depth
# first search cannot be used for that purpose.


# target node = u
# use queue
from collections import deque

def BFS(G,v,u):
    q = deque()  # create the empty queue
    visited = set() # visited set  
    steps = {v:0}   # number of edges

    visited.add(v)  # starting node v
    q.append(v)

    while q:   # while q is not empty
        w = q.popleft()
        if w == u:
            return steps[w]

        i = G.index[w]   # get row of w in the matrix
        for j in range(len(G.nodes)): # check every column in row i
            if G.M[i][j] is not None:
                x = G.nodes[j]
                if x not in visited:
                    visited.add(x)
                    steps[x] = steps[w] + 1
                    q.append(x)

    return None

# graph from task 2
class MatrixGraph:
    def __init__(self):
        self.index = {} # a dict, node label -> matrix position (used as both row and column index).
                        # Needed because labels may not be 0..n-1, and positions shift after removeNode.
        self.nodes = [] # list of nodes
        self.M = []  # list of lists: matrix itself

    def addNode(self,u):
        if u in self.index:
            return
        self.index[u] = len(self.nodes)
        self.nodes.append(u)
        for row in self.M:
            row.append(None)
        self.M.append([None] * len(self.nodes))

    def addEdge(self,u,v,w):
        self.addNode(u)
        self.addNode(v)  # if u, v is not in graph
        self.M[self.index[u]][self.index[v]] = w

    def removeNode(self,u):
        i = self.index.pop(u)  # get u's row number and remove it from dict
        self.M.pop(i) # remove the row
        for row in self.M:
            row.pop(i)   # remove the column
        self.nodes.pop(i)

        for k in range(i, len(self.nodes)):
            self.index[self.nodes[k]] = k   # the index of node after u decrease by 1


    def removeEdge(self,u,v):
        self.M[self.index[u]][self.index[v]] = None


# example to test
def test_bfs():
    G = MatrixGraph()
    #   A -> B -> C -> D
    #   A -> D            (shortcut)
    #   A -> E -> F
    #   Z                 (no edges, unreachable)
    G.addEdge("A", "B", 1)
    G.addEdge("B", "C", 1)
    G.addEdge("C", "D", 1)
    G.addEdge("A", "D", 1)
    G.addEdge("A", "E", 1)
    G.addEdge("E", "F", 1)
    G.addNode("Z")

    assert BFS(G, "A", "A") == 0      # start = target
    assert BFS(G, "A", "B") == 1
    assert BFS(G, "A", "C") == 2
    assert BFS(G, "A", "D") == 1      # finds the shortcut A->D, not A->B->C->D (3 edges)
    assert BFS(G, "A", "F") == 2
    assert BFS(G, "A", "Z") is None   # not reachable
    assert BFS(G, "D", "A") is None   # directed graph: no path back
    print("All BFS tests passed")

test_bfs()