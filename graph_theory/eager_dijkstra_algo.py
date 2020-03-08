from graph_theory.ds.graph import Graph
from graph_theory.ds.priority_queue import PriorityQueue
from typing import Dict, List, Tuple, Any
import math


class EagerDijkstra:

    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[str, bool] = dict([(key, False) for key in self.graph.nodes()])
        self.dist: Dict[str, float] = dict([(key, math.inf) for key in self.graph.nodes()])
        self.prev: Dict[Any, str] = dict([(key, -1) for key in self.graph.nodes()])
        self.pq = PriorityQueue[Tuple[str, float]](maxsize=len(self.graph.nodes()), sort_index=1)

    def run(self, start_node: str, end_node: str) -> Tuple[Dict[str, float], List[str]]:
        self.pq.insert((start_node, 0))
        self.visited[start_node] = True
        self.dist[start_node] = 0

        while not self.pq.is_empty():
            index, value = self.pq.pop()
            self.visited[index] = True
            edges = self.graph[index]
            for edge in edges:
                if self.visited[edge.to]: continue
                new_dist = edge.weight + self.dist[index]
                if new_dist < self.dist[edge.to]:
                    self.dist[edge.to] = new_dist
                    self.prev[edge.to] = index
                    if self.pq.contains(edge.to):
                        self.pq.update_key(edge.to, new_dist)
                    else:
                        self.pq.insert((edge.to, new_dist))
        return self.dist, self._shortestPath(start_node, end_node)

    def _shortestPath(self, start: str, end: str):
        path = []
        if self.dist[end] == math.inf: return path
        curr = end
        while curr != -1:
            path.append(curr)
            curr = self.prev[curr]
        return list(reversed(path))
