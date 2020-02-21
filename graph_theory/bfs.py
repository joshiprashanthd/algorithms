from ds.graph import Graph
from typing import Dict, List

class BFS:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[int, bool] = dict(
            [(key, False) for key in self.graph.nodes()])
        self.prev: Dict[int, int] = dict(
            [(key, -1) for key in self.graph.nodes()])
        self.queue: List[int] = []

    def run(self, start_node: int, end_node: int) -> list:
        self.__solve(start_node)
        path = self.__reconstructedPath(start_node, end_node)
        return path

    def __solve(self, start_node: int):
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
                                    
    def __reconstructedPath(self, start_node: int, end_node: int) -> list:
        path = []
        
        while end_node != -1:
            path.append(end_node)
            end_node = self.prev[end_node]
        
        path = list(reversed(path))
        
        if path[0] == start_node:
            return path
        return []


