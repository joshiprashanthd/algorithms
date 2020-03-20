from graph_theory.ds.graph import Graph
from typing import Dict, List, Any


class TarjanAlgorithm:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[Any, bool] = dict([(node, False) for node in self.graph.nodes()])
        self.ids: Dict[Any, int] = dict([(node, -1) for node in self.graph.nodes()])
        self.onStack: Dict[Any, bool] = dict([(node, False) for node in self.graph.nodes()])
        self.low_link: Dict[Any, int] = dict([(node, -1) for node in self.graph.nodes()])
        self.stack: List[Any] = []
        self.id: int = 0
        self.n_components: int = 0
        self.logic = False

    def run(self) -> Dict[Any, int]:
        for node in self.graph.nodes():
            if not self.visited[node]:
                self.__dfs(node)
        return self.low_link

    def __dfs(self, at: Any) -> None:
        self.id += 1
        self.visited[at] = True
        self.onStack[at] = True
        self.ids[at] = self.low_link[at] = self.id
        self.stack.append(at)

        for edge in self.graph[at]:
            if not self.visited[edge.to]: self.__dfs(edge.to)
            if self.onStack[edge.to]: self.low_link[at] = min(self.low_link[at], self.low_link[edge.to])

        # print("Stack: ", self.stack)
        if self.ids[at] == self.low_link[at]:
            node = self.stack.pop()
            while node != at:
                self.onStack[node] = False
                self.low_link[node] = self.ids[at]
                node = self.stack.pop()

            self.n_components += 1
