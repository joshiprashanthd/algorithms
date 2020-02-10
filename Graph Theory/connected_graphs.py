from graph import Graph
from typing import Dict
from dfs import DFS

class ConnectedGraph():
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[int, bool] = dict([(key, False) for key in self.graph.nodes()])
        self.component: Dict[int, int] = dict([(key, -1) for key in self.graph.nodes()])
        self.count = 0
        
    def run(self):
        for node in self.graph.nodes():
            if not self.visited[node]:
                self.count += 1
                self.__dfs(node)
            
        print("# OF COMPONENTS: {}".format(self.count))
        print("COMPONENTS ASSOCIATED WITH EACH NODE: \n", self.component)
        
    def __dfs(self, at):
        self.visited[at] = True
        
        self.component[at] = self.count
        edges = self.graph[at]
        
        for edge in edges:
            if not self.visited[edge.to]:
                self.__dfs(edge.to)
            
g = Graph[int]()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)

g.add_edge(8, 9)


cg = ConnectedGraph(g)
cg.run()