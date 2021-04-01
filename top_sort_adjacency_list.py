from adjacency_list_directed import graph as parentgraph

class graph(parentgraph):

    def top_sort(self):
        for i in range(1, self.N+1):
            if self.in_degree[i] == 0:
                self.dfs(i)

        self.sorted.reverse()
        for i in self.sorted:
            print(i, end=" ")

    def dfs(self, root):
        self.V = [False] * (self.N+1)
        self.sorted = []
        self.dfsrec(root)

    def dfsrec(self, root):
        self.V[root] = True
        for i in self.A[root]:
            if self.V[i] == False:
                self.dfsrec(i)
        self.sorted.append(root)


G = graph(5, [(1, 2), (2, 3), (1, 3), (1, 4), (3, 5)])
G.top_sort()
