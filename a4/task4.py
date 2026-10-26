# Implement Dijkstra’s algorithm on top of your graph data structure. Test it on a
# weighted graph of at least eight nodes, print the distances and one shortest path,
# and state the complexity of your implementation in terms of |V | and |E|.


def dijkstra(G, s):  # s is starting node
    # return dist (shortest distance from s to every node) and pred (predecessor of each node on a shortest path
    dist = {v: float("inf") for v in G.nodes}   # dist(v) is infinity
    pred = {v: None for v in G.nodes}    # pred(v) is undef
    dist[s] = 0                                 
    U = set(G.nodes)      # U = V (nodes not finished yet)

    while U:   # if U is empty then stop
        # find u in U with minimal dist u
        u = None
        for v in G.nodes:
            if v in U and (u is None or dist[v] < dist[u]):
                u = v
        if dist[u] == float("inf"):     # remaining nodes are unreachable so infinity
            break
        U.remove(u)                             

        # relax all edges (u, v) with v in U, scan row of u
        i = G.index[u]
        for j in range(len(G.nodes)):
            w = G.M[i][j]
            if w is None:
                continue     # no edge u so nodes[j]
            if w < 0:
                raise ValueError("Dijkstra requires non-negative weights")
            v = G.nodes[j]
            if v in U and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u

    return dist, pred


def shortest_path(pred, s, t):
    # backtrack the pred pointers from t to s
    path = []
    node = t
    while node is not None:
        path.append(node)
        node = pred[node]
    path.reverse()
    if path[0] != s:  # t is not reachable from s
        return None
    return path



# graph from task2
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
        if u not in self.index:  # if node doesnt exist
            return
        i = self.index.pop(u)  # get u's row number and remove it from dict
        self.M.pop(i) # remove the row
        for row in self.M:
            row.pop(i)   # remove the column
        self.nodes.pop(i)

        for k in range(i, len(self.nodes)):
            self.index[self.nodes[k]] = k   # the index of node after u decrease by 1


    def removeEdge(self,u,v):
        if u not in self.index or v not in self.index:
            return
        self.M[self.index[u]][self.index[v]] = None


# test
def test_dijkstra():
    G = MatrixGraph()
    for name in "ABCDEFGH":        # add nodes in this order (row 0..7)
        G.addNode(name)

    def undirected(u, v, w):   # undirected edge = two directed edges
        G.addEdge(u, v, w)
        G.addEdge(v, u, w)

    # graph from slide 
    undirected("A", "B", 2)
    undirected("A", "C", 3)
    undirected("A", "G", 7)
    undirected("B", "D", 1)
    undirected("B", "F", 5)
    undirected("B", "H", 1)
    undirected("B", "G", 4)
    undirected("C", "E", 3)
    undirected("D", "F", 1)
    undirected("F", "E", 1)
    undirected("G", "H", 2)
    undirected("G", "E", 1)

    dist, pred = dijkstra(G, "A")

    # print the distances
    print("Node  Distance  Predecessor")
    for v in G.nodes:
        print(f"{v:<6}{dist[v]:<10}{pred[v] or '-'}")

    # print one shortest path
    path = shortest_path(pred, "A", "E")
    print("\nShortest path A -> E:", " -> ".join(path), f"(length {dist['E']})")

    # check against the final table on slide 29
    assert dist == {"A": 0, "B": 2, "C": 3, "D": 3, "E": 5, "F": 4, "G": 5, "H": 3}
    assert pred == {"A": None, "B": "A", "C": "A", "D": "B",
                    "E": "F", "F": "D", "G": "H", "H": "B"}
    assert path == ["A", "B", "D", "F", "E"]

    # unreachable node
    G.addNode("Z")
    dist, pred = dijkstra(G, "A")
    assert dist["Z"] == float("inf")
    assert shortest_path(pred, "A", "Z") is None

    print("All Dijkstra tests passed")


test_dijkstra()