from graph import Graph
from typing import Dict, List
from queue import SimpleQueue


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

            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.queue.append(neighbor)
                    self.prev[neighbor] = current_node
                                    
    def __reconstructedPath(self, start_node: int, end_node: int) -> list:
        path = []
        
        while end_node != -1:
            path.append(end_node)
            end_node = self.prev[end_node]
        
        path = list(reversed(path))
        
        if path[0] == start_node:
            return path
        return []


g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 6)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(3, 6)
g.add_edge(4, 9)
g.add_edge(4, 6)
g.add_edge(4, 8)
g.add_edge(9, 8)
g.add_edge(5, 8)

bfs = BFS(g)
print(g)
print(bfs.run(1, 8))