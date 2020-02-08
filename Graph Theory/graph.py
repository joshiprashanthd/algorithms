from typing import Dict

class Graph(object):
    def __init__(self) -> None:
        self.graph: Dict[int, list] = dict()
        self.V: int = 0
        self.E: int = 0
    
    def add_edge_from(self, u: int, v: int, w: int = 0) -> None:
        self.graph.setdefault(u, [])
        self.graph[u].append((v, w))
        self._updateInfo()
        
    def add_edge(self, u: int, v: int, w: int = 0) -> None:
        self.graph.setdefault(u, [])
        self.graph.setdefault(v, [])
        self.graph[u].append(v)
        self.graph[v].append(u)
        self._updateInfo()
        
    def nodes(self) -> set:
        return list(self.graph.keys())
        
    def _updateInfo(self):
        self.V = max(list(self.graph.keys()))
        self.E = sum([len(adjacent_nodes) for adjacent_nodes in self.graph.values()])
        
    def __getitem__(self, name: int):
        return self.graph[name]
        
    def __str__(self):
        return self.graph.__str__()