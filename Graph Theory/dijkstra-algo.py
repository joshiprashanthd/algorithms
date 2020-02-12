from ds.priority_queue import PriorityQueue
from ds.graph import Graph
from typing import List, Dict, Tuple
import math
import queue

class Dijkstra:
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[str, bool] = dict([(key, False) for key in self.graph.nodes()])
        self.dist: Dict[str, float] = dict([(key, math.inf) for key in self.graph.nodes()])
        self.pq = PriorityQueue(maxsize=len(self.graph.nodes()))
    
    def run(self, start_node: str) -> None:
        self.pq.insert((start_node, 0))
        self.dist[0] = 0
        while not self.pq.is_empty():
            node, min_value = self.pq.pop()
            
            edges = self.graph[node]
            
            for edge in edges:
                if self.visited[edge.to]: continue
                new_dist = self.dist[node] + edge.weight
                if new_dist < self.dist[edge.to]:
                    self.dist[edge.to] = new_dist
                    self.pq.insert((edge.to, new_dist))
        return self.dist
    
    
g = Graph[int]()
g.add_edge_from(0, 1, 4)
g.add_edge_from(0, 2, 1)
g.add_edge_from(2, 1, 2)
g.add_edge_from(1, 3, 1)
g.add_edge_from(2, 3, 5)
g.add_edge_from(3, 4, 3)

print(g)

dj = Dijkstra(g)
print(dj.run(0))