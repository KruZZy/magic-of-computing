from adjacency_list import graph as parentgraph

class graph(parentgraph):
    def dfs(self, root):
        self.V = [False] * (self.N+1)
        self.dfsrec(root)

    def dfsrec(self, root):
        self.V[root] = True
        print(root, end=" ")
        for i in self.A[root]:
            if self.V[i] == False:
                self.dfsrec(i)


G = graph(4, [(1, 2), (1, 3), (1, 4), (2, 4)])
G.dfs(1)
