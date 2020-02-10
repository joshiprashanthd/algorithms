from typing import Dict, List, Generic, TypeVar
from edge import Edge

T = TypeVar('T')

class Graph(Generic[T], object):
    """
    Represents a graph using adjacency list.
    """
    
    def __init__(self) -> None:
        self.graph: Dict[T, List[Edge[T]]] = dict()
        self.V: int = 0
        self.E: int = 0
    
    def add_edge_from(self, u: T, v: T, w: float = 0) -> None:
        """
        Add a directed edge U -> V in the graph
        """
        self.graph.setdefault(u, [])
        self.graph.setdefault(v, [])
        
        self.graph[u].append(Edge[T](u, v, w))
        
        self._updateInfo(u, v)
        
    def add_edge(self, u: T, v: T, w: float = 0) -> None:
        self.graph.setdefault(u, [])
        self.graph.setdefault(v, [])
        
        self.graph[u].append(Edge[T](u, v, w))
        self.graph[v].append(Edge[T](v, u, w))
        
        self._updateInfo(u, v)
        
    def nodes(self) -> list:
        return list(self.graph.keys())
        
    def _updateInfo(self, u: T, v: T):
        self.V = len(list(self.graph.keys()))
        self.E = sum([len(adjacent_nodes) for adjacent_nodes in self.graph.values()])
        
    def __getitem__(self, name: T):
        return self.graph[name]
        
    def __str__(self):
        return '\n'.join(' | '.join(edge.__str__() for edge in self.graph[node]) for node in self.nodes())