from typing import Dict, List, Optional, Any, Tuple
from graph_theory.ds.graph import Graph, Edge
from graph_theory.ds.priority_queue import PriorityQueue


class LazyPrimsAlgorithm:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.n = len(self.graph.nodes())
        self.visited: Dict[Any, bool] = dict([(node, False) for node in self.graph.nodes()])
        self.pq: PriorityQueue = PriorityQueue[Tuple[Any, Any, float]](maxsize=100, sort_index=2)

    def __add_edges(self, node: Any) -> None:
        self.visited[node] = True
        for edge in self.graph[node]:
            if not self.visited[edge.to]:
                self.pq.insert((edge.from_, edge.to, edge.weight))

    def run(self, start_node: Any) -> Tuple[Optional[float], Optional[List[Edge]]]:
        if not start_node:
            start_node = self.graph.nodes()[0]
        m = self.n - 1  # Number of edges
        edge_count, total_cost, edges = 0, 0., []

        self.__add_edges(start_node)

        while (not self.pq.is_empty()) and edge_count != m:
            # Getting next edge having minimum cost
            from_, to, weight = self.pq.pop()

            # If the edge's destination already visited, then continue
            if self.visited[to]: continue

            # Otherwise, its our mst edge
            edges.append(Edge(from_, to, weight))
            edge_count += 1
            total_cost += weight

            # Add edges of the destination to the priority queue
            self.__add_edges(to)

        if edge_count != m:
            return None, None
        return total_cost, edges
