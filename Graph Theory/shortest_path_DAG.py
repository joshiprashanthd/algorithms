"""
A useful application of Topological Sort is to find shortest path the having minimum weight
to all the other nodes in the graph.
"""

import math
from ds.graph import Graph
from typing import List, Dict
from topoogical_sort import TopologicalSort

class DAGShortestPath:
    def __init__(self, graph: Graph):
        self.graph = graph
        tp_sort = TopologicalSort(self.graph)
        self.top_order = tp_sort.run()
        self.distance: Dict[str, float] = dict([(key, math.inf) for key in self.graph.nodes()]) 
        
        
    def run(self, start_node) -> Dict[str, float]:
        self.distance[start_node] = 0
        
        for i in range(len(self.top_order)):
            node_idx = self.top_order[i]
            
            for edge in self.graph[node_idx]:
                self.distance[edge.to] = min([edge.weight + self.distance[edge.from_], self.distance[edge.to]])
                
        return self.distance
    
    
g = Graph[str]()

g.add_edge_from('A', 'B', 3)
g.add_edge_from('A', 'C', 6)
g.add_edge_from('B', 'C', 4)
g.add_edge_from('B', 'D', 4)
g.add_edge_from('B', 'E', 11)
g.add_edge_from('C', 'D', 8)
g.add_edge_from('C', 'G', 11)
g.add_edge_from('D', 'E', -4)
g.add_edge_from('D', 'F', 5)
g.add_edge_from('D', 'G', 2)
g.add_edge_from('E', 'H', 9)
g.add_edge_from('F', 'H', 1)
g.add_edge_from('G', 'H', 2)

sp = DAGShortestPath(g)
print(g)
print(sp.run('A'))