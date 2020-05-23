from typing import Dict, List, Any

from graph_theory.ds.graph import Graph


class BFS:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[Any, bool] = dict(
            [(key, False) for key in self.graph.nodes()])
        self.prev: Dict[Any, int] = dict(
            [(key, -1) for key in self.graph.nodes()])
        self.queue: List[Any] = []

    def run(self, start_node: Any, end_node: Any) -> List[Any]:
        self.__solve(start_node)
        path = self.__reconstructedPath(start_node, end_node)
        return path

    def __solve(self, start_node: Any) -> None:
        self.queue.append(start_node)
        self.visited[start_node] = True

        while len(self.queue) != 0:
            current_node = self.queue.pop(0)

            edges = self.graph[current_node]

            for edge in edges:
                if not self.visited[edge.to]:
                    self.visited[edge.to] = True
                    self.queue.append(edge.to)
                    self.prev[edge.to] = current_node

    def __reconstructedPath(self, start_node: Any, end_node: Any) -> List[Any]:
        path = []

        while end_node != -1:
            path.append(end_node)
            end_node = self.prev[end_node]

        path = list(reversed(path))

        if path[0] == start_node:
            return path
        return []
