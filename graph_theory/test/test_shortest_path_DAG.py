import unittest

from graph_theory.ds.graph import Graph
from graph_theory.shortest_path_DAG import DAGShortestPath

class TestDAGShortestPath(unittest.TestCase):
    
    def setUp(self):
        self.g1 = Graph[str]()
        self.g1.add_edge('A', 'B', 3, directed=True)
        self.g1.add_edge('A', 'C', 6, directed=True)
        self.g1.add_edge('B', 'C', 4, directed=True)
        self.g1.add_edge('B', 'D', 4, directed=True)
        self.g1.add_edge('B', 'E', 11, directed=True)
        self.g1.add_edge('C', 'D', 8, directed=True)
        self.g1.add_edge('C', 'G', 11, directed=True)
        self.g1.add_edge('D', 'E', -4, directed=True)
        self.g1.add_edge('D', 'F', 5, directed=True)
        self.g1.add_edge('D', 'G', 2, directed=True)
        self.g1.add_edge('E', 'H', 9, directed=True)
        self.g1.add_edge('F', 'H', 1, directed=True)
        self.g1.add_edge('G', 'H', 2, directed=True)
        
    def test_1(self):
        sp = DAGShortestPath(self.g1)
        self.assertEqual({'A': 0, 'B': 3, 'C': 6, 'D': 7, 'E': 3, 'G': 9, 'F': 12, 'H': 11}, sp.run('A'))
        
if __name__ == "__main__":
    unittest.main()