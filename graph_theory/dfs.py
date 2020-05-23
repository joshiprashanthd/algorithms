from typing import Dict, List, Any

from graph_theory.ds.graph import Graph


class DFS:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.visited: Dict[Any, bool] = dict([(key, False) for key in graph.nodes()])
        self.visited_nodes: List[Any] = []

    def run(self) -> List[Any]:
        self.run_util(self.graph.nodes()[0])
        return self.visited_nodes

    def run_util(self, at: Any) -> None:
        if self.visited[at]: return
        self.visited[at] = True
        self.visited_nodes.append(at)

        edges = self.graph[at]
        for edge in edges:
            self.run_util(edge.to)
