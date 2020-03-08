import math
from typing import List, get_type_hints, Tuple, Optional

from graph_theory.ds.graph import Graph


class FloydWarshallAlgorithm:

    def __init__(self, graph: Graph):
        self.graph = graph
        self.n = self.graph.V
        self.dp = [[math.inf for j in range(self.n)] for i in range(self.n)]
        self.next = [[-1 for j in range(self.n)] for i in range(self.n)]

    def __setup(self, m: List[List[int]]) -> None:
        for i in range(self.n):
            for j in range(self.n):
                self.dp[i][j] = m[i][j]
                if m[i][j] != math.inf:
                    self.next[i][j] = j

    def run(self, start_node: int, end_node: int) -> Optional[Tuple[List[int], float]]:
        m = self.graph.to_matrix()
        self.__setup(m)

        for k in range(1, self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.next[i][j] = self.next[i][k]
                        self.dp[i][j] = self.dp[i][k] + self.dp[k][j]
        self.__propagate_negative_cycle()
        return self.__reconstruct_path(start_node, end_node)

    def __propagate_negative_cycle(self) -> None:
        for k in range(1, self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][j] > self.dp[i][k] + self.dp[k][j]:
                        self.next[i][j] = -1
                        self.dp[i][j] = -math.inf

    def __reconstruct_path(self, start: int, end: int) -> Optional[Tuple[List[int], float]]:
        path: List[int] = []
        if self.dp[start][end] == math.inf: return path, 0

        at = start
        cost: float = 0

        while at != end:
            if at == -1: return None
            path.append(at)
            cost += self.dp[at][self.next[at][end]]
            at = self.next[at][end]
        path.append(end)
        return path, cost
