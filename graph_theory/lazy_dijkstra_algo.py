from graph_theory.ds.priority_queue import PriorityQueue
from graph_theory.ds.graph import Graph
from typing import List, Dict, Tuple, Union
import math


class LazyDijkstra:

    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[str, bool] = dict([(key, False) for key in self.graph.nodes()])
        self.dist: Dict[str, float] = dict([(key, math.inf) for key in self.graph.nodes()])
        self.prev: Dict[str, str] = dict([(key, -1) for key in self.graph.nodes()])
        self.pq = PriorityQueue[Tuple[int, int]](maxsize=len(self.graph.nodes()), sort_index=1)

    def run(self, start_node: str, end_node: str) -> Tuple[Dict[str, float], List[str]]:
        self.__compute_dist_prev(start_node)
        return self.dist, self.__shortest_path(end_node)

    def __compute_dist_prev(self, start_node: str):
        self.pq.insert((start_node, 0))
        self.dist[start_node] = 0

        while not self.pq.is_empty():
            node, value = self.pq.pop()
            self.visited[node] = True

            edges = self.graph[node]
            for edge in edges:
                if self.visited[edge.to]: continue
                new_dist = self.dist[node] + edge.weight
                if new_dist < self.dist[edge.to]:
                    self.dist[edge.to] = new_dist
                    self.prev[edge.to] = node
                    self.pq.insert((edge.to, new_dist))

    def __shortest_path(self, end: Union[str, int]):
        path = []
        if self.dist[end] == math.inf: return path
        curr = end
        while curr != -1:
            path.append(curr)
            curr = self.prev[curr]
        return list(reversed(path))

    def gen_path(self, start: Union[str, int], end: Union[str, int]):
        self.__compute_dist_prev(start)
        if self.dist[end] == math.inf: yield None
        curr = end
        while True:
            if curr == -1:
                yield None
            else:
                yield curr
            curr = self.prev[curr]
