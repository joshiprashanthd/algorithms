from .graph_base import Graph

class AdjacencyGraph(Graph):
    def __init__(self, name):
        super().__init__(name)

    def add_edge(self, u, v):
        if v not in self.adj[u]:
            self.adj[u].append(v)
            self.edges.append((u, v)) 
