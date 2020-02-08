from graph import Graph
from typing import Dict

class DFS:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.visited: Dict[int, bool] = dict([(key, False) for key in graph.nodes()])
    
    def run(self) -> None:
        self.run_util(self.graph.nodes()[0])
        
        
    def run_util(self, at):
        if self.visited[at]: return
        self.visited[at] = True

        neighbors = self.graph[at]
        for neighbor in neighbors:
            self.run_util(neighbor)
    
g = Graph()
g.add_edge(5, 2)
g.add_edge(4, 8)
g.add_edge(2, 1)
g.add_edge(1, 8)
g.add_edge(2, 9)

dfs = DFS(g)
dfs.run()
