class graph(object):

    def __init__(self, nodes, edge_list = None):
        self.N = nodes
        self.A = [[False for i in range(self.N+1)] for j in range(self.N+1)] # initialise the adjacency matrix as an (N+1)*(N+1) array, so we can use indexes from 1.
        if edge_list != None: # let's optionally give this class a list of tuples, consisting of the edges, as a little Python exercise.
            for x in edge_list:
                self.set_edge(x)

    def is_valid_tuple(self, x):
        return isinstance(x, tuple) and len(x) == 2 and all((a > 0 and a <= self.N) for a in x)
        # this function checks whether an element is a tuple meant to describe a graph edge.
        # the conditions are as follows: the tuple is of length 2, and both its elements are between 1 and N.

    def set_edge(self, e, status = True):
        # set_edge(edge, True) adds the edge to the graph.
        # set_edge(edge, False) removes the edge from the graph.
        if self.is_valid_tuple(e) == False:
            print("element", e, "is not formatted correctly.")
        else:
            self.A[e[0]][e[1]], self.A[e[1]][e[0]] = status, status

    def get_edges(self):
        for i in range(1, self.N+1):
            for j in range(i, self.N+1): ## we start the column loop from i, so we don't treat
                if self.A[i][j]: print("edge from ", i, "to", j)


G = graph(3, [(1, 2), (2, 3)])
G.get_edges()
