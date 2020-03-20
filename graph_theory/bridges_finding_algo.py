from graph_theory.ds.graph import Graph
from typing import Dict, List, Any


class BridgesFindingAlgorithm:

    def __init__(self, graph: Graph):
        self.graph = graph
        self.id = 0
        self.ids: Dict[Any, int] = dict([(node, 0) for node in self.graph.nodes()])
        self.visited: Dict[Any, bool] = dict([(node, False) for node in self.graph.nodes()])
        self.low_link: Dict[Any, int] = dict([(node, 0) for node in self.graph.nodes()])

    def run(self) -> List[Any]:
        bridges: List[Any] = []
        for node in self.graph.nodes():
            if not self.visited[node]:
                self.__dfs(node, -1, bridges)
        return bridges

    def __dfs(self, at: Any, parent: Any, bridges: List[Any]) -> None:
        self.visited[at] = True
        self.id += 1
        self.ids[at] = self.low_link[at] = self.id

        for edge in self.graph[at]:
            if edge.to == parent: continue
            if not self.visited[edge.to]:
                self.__dfs(edge.to, at, bridges)
                self.low_link[at] = min(self.low_link[edge.to], self.low_link[at])
                if self.ids[at] < self.low_link[edge.to]:
                    bridges.append(at)
                    bridges.append(edge.to)
            else:
                self.low_link[at] = min(self.ids[edge.to], self.low_link[at])
