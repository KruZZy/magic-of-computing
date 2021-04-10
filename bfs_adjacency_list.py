from adjacency_list import graph as parentgraph
from collections import deque

class graph(parentgraph):
    def bfs(self, root):
        queue = deque([root])
        visited = [False] * (self.N+1)
        visited[root] = True
        while queue:
            current = queue.popleft()
            print(current, end=" ")
            for i in self.A[current]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)

G = graph(4, [(1, 2), (1, 3), (1, 4), (2, 4)])
G.bfs(1)
