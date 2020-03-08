"""
A useful application of Topological Sort is to find shortest path the having minimum weight
to all the other nodes in the graph.
"""

import math
from graph_theory.ds.graph import Graph
from typing import List, Dict
from graph_theory.topoogical_sort import TopologicalSort


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
