from typing import Dict, List, Any, Set, Union
from copy import deepcopy

from graph_theory.ds.graph import Graph


class KahnsAlgorithm:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.top_order: List[Any] = []
        self.s: Set[Any] = set([node for node in self.graph.nodes() if self.graph.get_indegrees(node) == 0])

    def run(self) -> Union[None, List[Any]]:
        while len(self.s) > 0:
            node = self.s.pop()
            self.top_order.append(node)
            edges = self.graph[node]
            for edge in edges[:]:
                self.graph.remove_edge(edge.from_, edge.to)
                if self.graph.get_indegrees(edge.to) == 0:
                    self.s.add(edge.to)

        if len(self.graph.edges()) > 0:
            return None
        else:
            return self.top_order
