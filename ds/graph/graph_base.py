from collections import defaultdict 

class Graph:
    def __init__(self, name) -> None:
        self.name = name
        self.edges = []
        self.adj = defaultdict(lambda : [])

    @property
    def vertices(self):
        return list(self.adj.keys())

    def add_edge(self, u, v):
        raise NotImplementedError()

