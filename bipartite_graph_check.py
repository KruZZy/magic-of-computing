from adjacency_list import graph as parentgraph
from collections import deque

WHITE = 0
RED = 1
BLUE = 2

class graph(parentgraph):
    def print_nodes_with_colour(self, col):
        for i in range(1, self.N+1):
            if self.col[i] == col:
                print(i, end=" ")
        print()
    def is_bipartite(self):
        self.col = [WHITE] * (self.N+1)
        bipart = True
        for i in range(1, self.N+1):
            if self.col[i] == WHITE:
                if self.bfs(i) == False:
                    bipart = False
                    break
        if bipart:
            print("The graph is bipartite. Sets: ")
            self.print_nodes_with_colour(RED)
            self.print_nodes_with_colour(BLUE)
        else:
            print("The graph is not bipartite.")

    def bfs(self, root):
        queue = deque([root])
        self.col[root] = RED
        while queue:
            current = queue.popleft()
            neigh_col = RED if self.col[current] == BLUE else BLUE

            for i in self.A[current]:
                if self.col[i] == WHITE:
                    self.col[i] = neigh_col
                    queue.append(i)
                elif self.col[i] != neigh_col:
                    return False
        return True

G = graph(7, [(1, 4), (1, 5), (2, 3), (2, 4), (6, 7)])
G.is_bipartite()
