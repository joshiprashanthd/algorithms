import math
from typing import Dict, Any

from graph_theory.ds.graph import Graph


class BellmanFordAlgorithm:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.dist: Dict[Any, float] = dict([(node, math.inf) for node in self.graph.nodes()])

    def run(self, start_node: Any) -> Dict[Any, float]:
        V = self.graph.V
        self.dist[start_node] = 0

        # Relaxation of every edge
        for _ in range(V):
            for edge in self.graph.edges():
                new_dist = self.dist[edge.from_] + edge.weight
                if new_dist < self.dist[edge.to]:
                    self.dist[edge.to] = new_dist

        # propagating negative cycles
        # since we have already gotten the optimal distance from one node to every other node
        # so now we again try to relax every node, if a distance from any node to a certain destination node reduces
        # this means there is a negative cycle.
        for _ in range(V):
            for edge in self.graph.edges():
                new_dist = self.dist[edge.from_] + edge.weight
                if new_dist < self.dist[edge.to]:
                    self.dist[edge.to] = -math.inf

        return self.dist
