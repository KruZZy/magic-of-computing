from adjacency_list_weighted import graph as parentgraph
from queue import PriorityQueue

oo = 1 << 25 ## this is the big value we will assign to the start costs - bit 1 moved 25 positions, meaning 2 to the power of 25.

class graph(parentgraph):
    def shortest_path(self, start, finish):
        pq = PriorityQueue()

        cost = [oo] * (self.N+1)
        visited = [False] * (self.N+1)
        self.parent = [0] * (self.N+1)
        cost[start] = 0 # we initialise the cost of the start node with 0.
        pq.put((0, start)) # the PriorityQueue collection orders tuples in ascending order by the first element, by default.

        while pq.empty() == False:
            u = pq.get()[1] # get second element from the tuple
            if visited[u]:
                continue # we skip if we have already processed another route through this node
            for i in self.A[u]:
                v = i[0] # the neighbouring node
                w = i[1] # the cost of the edge

                if cost[v] > cost[u] + w:

                    cost[v] = cost[u] + w
                    self.parent[v] = u
                    pq.put((cost[v], v))

            visited[u] = True

        print("Smallest path cost is ", cost[finish])
        self.get_source(finish)

    def get_source(self, node):
        if self.parent[node] != 0:
            self.get_source(self.parent[node])
        print(node, end=" ")

G = graph(5, [(1, 2, 4), (1, 4, 2), (1, 3, 15), (2, 5, 10), (2, 4, 5), (5, 3, 12), (4, 3, 5)])
G.shortest_path(1, 3)
