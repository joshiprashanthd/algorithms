from typing import List, Dict, Any

from graph_theory.ds.graph import Graph


class TopologicalSort:
    def __init__(self, graph: Graph) -> None:
        self.graph: Graph = graph
        self.top_rev_order: List[Any] = []
        self.visited: Dict[Any, bool] = dict([(key, False) for key in self.graph.nodes()])

    def run(self) -> List[Any]:
        for node in self.graph.nodes():
            if not self.visited[node]:
                visited_nodes = []
                self.__dfs(node, visited_nodes)
                for node in visited_nodes:
                    self.top_rev_order.append(node)
        self.top_rev_order.reverse()
        return self.top_rev_order

    def __dfs(self, at: Any, visited_nodes: List[Any]) -> None:
        self.visited[at] = True

        edges = self.graph[at]

        for edge in edges:
            if not self.visited[edge.to]:
                self.__dfs(edge.to, visited_nodes)

        visited_nodes.append(at)
