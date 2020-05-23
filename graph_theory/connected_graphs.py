from typing import Dict, Any

from graph_theory.ds.graph import Graph


class ConnectedGraph():
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[Any, bool] = dict([(key, False) for key in self.graph.nodes()])
        self.component: Dict[Any, int] = dict([(key, -1) for key in self.graph.nodes()])
        self.count = 0

    def run(self):
        for node in self.graph.nodes():
            if not self.visited[node]:
                self.count += 1
                self.__dfs(node)

        return self.count, self.component

    def __dfs(self, at: Any) -> None:
        self.visited[at] = True

        self.component[at] = self.count
        edges = self.graph[at]

        for edge in edges:
            if not self.visited[edge.to]:
                self.__dfs(edge.to)
