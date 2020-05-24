from typing import Dict, List, Any

from graph_theory.ds.graph import Graph


class EulerianPathFinder:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[Any, bool] = dict([(node, False) for node in self.graph.nodes()])
        self.out_degrees: Dict[Any, int] = dict([(node, 0) for node in self.graph.nodes()])
        self.in_degrees: Dict[Any, int] = dict([(node, 0) for node in self.graph.nodes()])
        self.path = []

    def __verify(self) -> bool:
        start_nodes, end_nodes = 0, 0
        for node in self.graph.nodes():
            if self.out_degrees[node] - self.in_degrees[node] > 1 or self.in_degrees[node] - self.out_degrees[node] > 1:
                return False
            if self.out_degrees[node] - self.in_degrees[node] == 1:
                start_nodes += 1
            if self.in_degrees[node] - self.out_degrees[node] == 1:
                end_nodes += 1
        return (end_nodes == 0 and start_nodes == 0) or (end_nodes == 1 and start_nodes == 1)

    def __count_degrees(self):
        for node in self.graph.nodes():
            self.out_degrees[node] = self.graph.get_outdegrees(node)
            self.in_degrees[node] = self.graph.get_indegrees(node)

    def __find_start_node(self) -> Any:
        start = 0
        for node in self.graph.nodes():
            if self.out_degrees[node] - self.in_degrees[node] == 1: return node
            if self.out_degrees[node] > 0: start = node
        return start

    def run(self) -> List[Any]:
        self.__count_degrees()
        if self.__verify():
            start_node = self.__find_start_node()
            self.__dfs(start_node)
        else:
            print("Graph does not have any eulerian path.")
            return None
        return self.path if len(self.path) == self.graph.E + 1 else None

    def __dfs(self, at: Any):
        while self.out_degrees[at] != 0:
            self.out_degrees[at] -= 1
            self.__dfs(self.graph[at][self.out_degrees[at]].to)
        self.path.insert(0, at)
