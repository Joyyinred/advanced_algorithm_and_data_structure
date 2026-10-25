#Implement a graph data structure with addNode(u), addEdge(u,v,w), removeNode(u)
#and removeEdge(u,v), this time using an adjacency matrix as the underlying representation. Compare the memory consumption and the runtime of addEdge and
#removeNode with an adjacency list implementation, and state for which kind of
#graphs you would choose which representation. Provide a test that shows that all
#methods work.

# implementation with matrix
# do it in directed graph since task 4 need to implement Dijkstra’s algorithm
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

# implementation with adj list(addedge, removenode)
class AdjListGraph:
    def __init__(self):
        self.adj = []  # dict of list of (neighbour, weight)

    def addNode(self,u):
        self.adj.append(u)

    def addEdge(self,u,v,w):
        self.adj[u][v] = w

def test_matrix_graph():
    G = MatrixGraph()

    # helper: read the weight of edge u -> v directly from the matrix (None = no edge)
    def edge(u, v):
        return G.M[G.index[u]][G.index[v]]

    #  addNode 
    G.addNode("A")
    G.addNode("B")
    G.addNode("C")
    assert G.nodes == ["A", "B", "C"]
    assert G.index == {"A": 0, "B": 1, "C": 2}
    assert len(G.M) == 3 and all(len(row) == 3 for row in G.M)   # matrix is 3x3
    assert all(x is None for row in G.M for x in row)            # no edges yet

    G.addNode("A")                                   # adding an existing node changes nothing
    assert G.nodes == ["A", "B", "C"]
    print("addNode works")

    #  addEdge 
    G.addEdge("A", "B", 5)
    G.addEdge("B", "C", -2)                          # negative weight
    G.addEdge("C", "A", 0)                           # weight 0 is still an edge
    assert edge("A", "B") == 5
    assert edge("B", "C") == -2
    assert edge("C", "A") == 0
    assert edge("B", "A") is None                    # directed: no edge in the opposite direction

    G.addEdge("D", "C", 7)                           # D does not exist yet -> created automatically
    assert G.nodes == ["A", "B", "C", "D"]
    assert len(G.M) == 4 and all(len(row) == 4 for row in G.M)   # matrix grew to 4x4
    assert edge("D", "C") == 7

    G.addEdge("A", "B", 9)                           # adding the same edge again updates the weight
    assert edge("A", "B") == 9
    print("addEdge works")

    #  removeEdge 
    G.removeEdge("A", "B")
    assert edge("A", "B") is None
    assert edge("B", "C") == -2                      # other edges are untouched
    print("removeEdge works")

    #  removeNode 
    G.addEdge("A", "B", 3)                           # add edges into and out of B again
    # now: A->B (3), B->C (-2), C->A (0), D->C (7)
    G.removeNode("B")

    assert "B" not in G.index and "B" not in G.nodes
    assert G.nodes == ["A", "C", "D"]
    assert G.index == {"A": 0, "C": 1, "D": 2}       # C and D were re-indexed
    assert len(G.M) == 3 and all(len(row) == 3 for row in G.M)   # matrix shrank to 3x3

    # edges not involving B still exist and are found at their new positions
    assert edge("C", "A") == 0
    assert edge("D", "C") == 7
    # no other edges remain (A->B and B->C are gone with B)
    edges = [(G.nodes[i], G.nodes[j], G.M[i][j])
             for i in range(len(G.nodes)) for j in range(len(G.nodes))
             if G.M[i][j] is not None]
    assert sorted(edges) == [("C", "A", 0), ("D", "C", 7)]
    print("removeNode works")

    #  remove first and last node 
    G.removeNode("A")                                # first node
    assert G.index == {"C": 0, "D": 1}
    assert edge("D", "C") == 7
    G.removeNode("D")                                # last node
    assert G.nodes == ["C"] and G.M == [[None]]
    print("removing first/last node works")

    print("All tests passed")


test_matrix_graph()



    