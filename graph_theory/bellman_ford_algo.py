from graph_theory.ds.graph import Graph
from typing import Dict, List
import math


class BellmanFordAlgorithm:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.dist: Dict[str, float] = dict([(node, math.inf) for node in self.graph.nodes()])

    def run(self, start_node: str) -> Dict[str, float]:
        V = self.graph.V
        self.dist[start_node] = 0

        # Relaxation of every edge
        for _ in range(V):
            for edge in self.graph.edges():
                new_dist = self.dist[edge.from_] + edge.weight
                if new_dist < self.dist[edge.to]:
                    self.dist[edge.to] = new_dist

        for _ in range(V):
            for edge in self.graph.edges():
                new_dist = self.dist[edge.from_] + edge.weight
                if new_dist < self.dist[edge.to]:
                    self.dist[edge.to] = -math.inf

        return self.dist
