from collections import defaultdict

class graph(object):

    def __init__(self, nodes, edge_list = None):
        self.N = nodes
        self.A = defaultdict(list)
        if edge_list != None: # let's optionally give this class a list of tuples, consisting of the edges, as a little Python exercise.
            for x in edge_list:
                self.add_edge(x)

    def is_valid_tuple(self, x):
        return isinstance(x, tuple) and len(x) == 3 and all((a > 0 and a <= self.N) for a in x[0:2])
        # this function checks whether an element is a tuple meant to describe a weighted graph edge.
        # the conditions are as follows: the tuple is of length 3, and its first and second elements are between 1 and N.
        # in our case, there is no condition on the weight of the edge.

    def add_edge(self, e):
        if self.is_valid_tuple(e):
            if e[0] not in self.A[e[1]]:
                self.A[e[0]].append((e[1], e[2]))
                self.A[e[1]].append((e[0], e[2]))
        else: print("element", e, "is not formatted correctly!")

    def remove_edge(self, e):
        if self.is_valid_tuple(e):
            if e[0] in self.A[e[1]]:
                self.A[e[0]].remove((e[1], e[2]))
                self.A[e[1]].remove((e[0], e[2]))
        else: print("element", e, "is not formatted correctly!")
