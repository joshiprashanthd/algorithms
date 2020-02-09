from graph import Graph
from typing import List, Dict

class TopologicalSort:
    def __init__(self, graph: Graph) -> None:
        self.graph: Graph = graph
        self.top_rev_order: List[int] = []
        self.visited: Dict[int, bool] = dict([(key, False) for key in self.graph.nodes()])
        
        
    def run(self):
        
        for node in self.graph.nodes():
            if not self.visited[node]:
                visited_nodes = []
                self.__dfs(node, visited_nodes)
                for node in visited_nodes:
                    self.top_rev_order.append(node)
        # self.top_rev_order.reverse()
        print("TOPOLOGICAL ORDER: ", self.top_rev_order)
    
    def __dfs(self, at: int, visited_nodes: list):
        self.visited[at] = True
        visited_nodes.append(at)
        
        neighbors = self.graph[at]
        
        for neighbor in neighbors:
            if not self.visited[neighbor]:
                self.__dfs(neighbor, visited_nodes)
            
g = Graph()
g.add_edge_from(1, 3)
g.add_edge_from(1, 2)
g.add_edge_from(3, 5)
g.add_edge_from(2, 5)
g.add_edge_from(2, 6)

ts = TopologicalSort(g)
ts.run()