from typing import Dict, List, Generic, TypeVar, Union, NoReturn
import math

T = TypeVar('T', int, str, float)
Matrix = Union[List[List[Union[int, float]]], NoReturn]


class Edge(Generic[T]):
    def __init__(self, from_: T, to: T, weight: float = 0):
        self.from_: T = from_
        self.to: T = to
        self.weight = weight

    def __str__(self):
        return f"{self.from_}" + " -" + f"{self.weight}" + "-> " + f"{self.to}"


class Graph(Generic[T], object):
    """
    Represents a graph using adjacency list.
    """

    def __init__(self) -> None:
        self.graph: Dict[T, List[Edge[T]]] = dict()
        self.V: int = 0
        self.E: int = 0

    def add_edge(self, u: T, v: T, w: Union[int, float] = 0, directed: bool = False) -> None:
        self.graph.setdefault(u, [])
        self.graph.setdefault(v, [])

        self.graph[u].append(Edge[T](u, v, w))
        if not directed:
            self.graph[v].append(Edge[T](v, u, w))

        self.__updateInfo(u, v)

    def remove_edge(self, u: T, v: T, directed: bool = False) -> None:
        if u in self.nodes() and v in self.nodes():
            for edge in self.graph[u]:
                if edge.to == v:
                    self.graph[u].remove(edge)
                    break
            if not directed:
                for edge in self.graph[v]:
                    if edge.to == u:
                        self.graph[v].remove(edge)
                        break
        self.__updateInfo(u, v)

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

    def __updateInfo(self, u: T, v: T):
        # self.V = int(max(self.graph.keys()) + 1)
        self.E = sum([len(adjacent_nodes)
                      for adjacent_nodes in self.graph.values()])

    def __getitem__(self, name: T):
        return self.graph[name]

    def __str__(self):
        return '\n'.join(' | '.join(edge.__str__() for edge in self.graph[node]) for node in self.nodes())