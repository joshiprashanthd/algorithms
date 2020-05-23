import math
from typing import List, Tuple, Any

from graph_theory.ds.graph import Graph


class FloydWarshallAlgorithm:

    def __init__(self, graph: Graph):
        self.graph = graph
        self.n = self.graph.V
        self.dp = [[math.inf for j in range(self.n)] for i in range(self.n)]
        self.next = [[-1 for j in range(self.n)] for i in range(self.n)]

    def __setup(self, m: List[List[Any]]) -> None:
        for i in range(self.n):
            for j in range(self.n):
                self.dp[i][j] = m[i][j]
                if m[i][j] != math.inf:
                    self.next[i][j] = j

    def run(self, start_node: Any, end_node: Any) -> Tuple[List[Any], float]:
        m = self.graph.to_matrix()
        self.__setup(m)
        self.__compute_dp_table()
        self.__propagate_negative_cycle()
        return self.__reconstruct_path(start_node, end_node)

    def __compute_dp_table(self):
        for k in range(1, self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.next[i][j] = self.next[i][k]
                        self.dp[i][j] = self.dp[i][k] + self.dp[k][j]

    def __propagate_negative_cycle(self) -> None:
        for k in range(1, self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][j] > self.dp[i][k] + self.dp[k][j]:
                        self.next[i][j] = -1
                        self.dp[i][j] = -math.inf

    def __reconstruct_path(self, start: Any, end: Any) -> Tuple[List[Any], float]:
        path = []
        if self.dp[start][end] == math.inf: return path, 0

        at = start
        cost = 0.

        while at != end:
            if at == -1: return None
            path.append(at)
            cost += self.dp[at][self.next[at][end]]
            at = self.next[at][end]
        path.append(end)
        return path, cost

    def gen_path(self, start: int, end: int):
        m = self.graph.to_matrix()
        self.__setup(m)
        self.__compute_dp_table()
        self.__propagate_negative_cycle()
        print("dp: ", self.dp)
        print("start: ", start)
        print("end: ", end)
        if self.dp[start][end] == math.inf: yield None

        at = start

        while True:
            if at == -1:
                yield None
            else:
                yield at
            at = self.next[at][end]
