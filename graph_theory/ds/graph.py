import math
from typing import Dict, List, Generic, TypeVar, Union, NoReturn

T = TypeVar('T', int, str, float)
Matrix = Union[List[List[Union[int, float]]], NoReturn]


class Edge(Generic[T]):
    def __init__(self, from_: T, to: T, weight: float = 0):
        self.from_: T = from_
        self.to: T = to
        self.weight = weight

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return self.from_ == other.from_ and self.to == other.to and self.weight == other.weight

    def __str__(self):
        return f"Edge({self.from_}, {self.to}, {self.weight})"

    def __repr__(self):
        return f"Edge({self.from_}, {self.to}, {self.weight})"


class Graph(Generic[T], object):
    """
    Represents a graph using adjacency list.
    """

    def __init__(self, directed=True) -> None:
        self.graph: Dict[T, List[Edge[T]]] = dict()
        self.__degrees: Dict[T, List[int, int]] = dict()
        self.directed = directed
        self.V: int = 0
        self.E: int = 0

    def add_edge(self, u: T, v: T, w: Union[int, float] = 0) -> None:
        self.graph.setdefault(u, [])
        self.graph.setdefault(v, [])
        self.__degrees.setdefault(u, [0, 0])
        self.__degrees.setdefault(v, [0, 0])

        self.graph[u].append(Edge[T](u, v, w))
        self.__degrees[u][1] += 1
        self.__degrees[v][0] += 1
        if not self.directed:
            self.graph[v].append(Edge[T](v, u, w))
            self.__degrees[u][0] += 1
            self.__degrees[v][1] += 1
        self.__updateInfo(u, v)

    def remove_edge(self, u: T, v: T) -> None:
        if u in self.nodes() and v in self.nodes():
            for edge in self.graph[u]:
                if edge.to == v:
                    self.graph[u].remove(edge)
                    self.__degrees[v][0] -= 1
                    self.__degrees[u][1] -= 1
                    break
            if not self.directed:
                for edge in self.graph[v]:
                    if edge.to == u:
                        self.graph[v].remove(edge)
                        self.__degrees[u][0] -= 1
                        self.__degrees[v][1] -= 1
                        break
        self.__updateInfo(u, v)

    def get_indegrees(self, u: T):
        return self.__degrees[u][0]

    def get_outdegrees(self, u: T):
        return self.__degrees[u][1]

    def nodes(self) -> list:
        return list(self.graph.keys())

    def edges(self) -> list:
        return list([edge for node in self.nodes() for edge in self.graph[node]])

    def to_matrix(self) -> Matrix:
        m: Matrix = [[math.inf for j in range(
            self.V)] for i in range(self.V)]
        for node in range(self.V):
            if node not in self.graph.keys():
                continue
            for edge in self.graph[node]:
                m[node][edge.to] = edge.weight
        return m

    @staticmethod
    def from_matrix(matrix: Matrix):
        graph = Graph[int]()
        n_vertices = len(matrix)
        for src in range(n_vertices):
            for dest in range(n_vertices):
                if matrix[src][dest] != 0:
                    graph.add_edge(src, dest, matrix[src][dest])
        return graph

    def __updateInfo(self, u: T, v: T):
        if not isinstance(list(self.graph.keys())[0], str):
            self.V = int(max(self.graph.keys()) + 1)
        self.E = sum([len(adjacent_nodes)
                      for adjacent_nodes in self.graph.values()])

    def __getitem__(self, name: T):
        return self.graph[name]

    def __str__(self):
        return '\n'.join(' | '.join(edge.__str__() for edge in self.graph[node]) for node in self.nodes())
