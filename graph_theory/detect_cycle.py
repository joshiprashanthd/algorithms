from typing import Dict, List, Any

from graph_theory.ds.graph import Graph


class DetectCycle:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[Any, bool] = dict([(node, False) for node in self.graph.nodes()])
        self.recursion_stack: Dict[Any, bool] = dict([(node, False) for node in self.graph.nodes()])

    def __dfs(self, at: Any) -> bool:
        self.visited[at] = True
        self.recursion_stack[at] = True

        edges = self.graph[at]
        for edge in edges:
            if not self.visited[edge.to]:
                if self.__dfs(edge.to):
                    return True
            elif self.recursion_stack[edge.to]:
                return True

        self.recursion_stack[at] = False
        return False

    def run(self) -> bool:
        for node in self.graph.nodes():
            if not self.visited[node]:
                if self.__dfs(node):
                    return True
        return False
