import unittest
import math

from graph_theory.ds.graph import Graph
from graph_theory.bellman_ford_algo import BellmanFordAlgorithm

class TestBellmanFordAlgorithm(unittest.TestCase):
    
    def setUp(self):
        self.g1 = Graph[int]()
        self.g1.add_edge(0, 1, 1, directed=True)
        self.g1.add_edge(1, 2, 1, directed=True)
        self.g1.add_edge(2, 4, 1, directed=True)
        self.g1.add_edge(4, 3, -3, directed=True)
        self.g1.add_edge(3, 2, 1, directed=True)
        self.g1.add_edge(1, 5, 4, directed=True)
        self.g1.add_edge(1, 6, 4, directed=True)
        self.g1.add_edge(5, 6, 5, directed=True)
        self.g1.add_edge(6, 7, 4, directed=True)
        self.g1.add_edge(5, 7, 3, directed=True)
        
        self.g2 = Graph[int]()
        self.g2.add_edge(0, 1, 1, directed=True)
        self.g2.add_edge(0, 2, 1, directed=True)
        self.g2.add_edge(1, 3, 4, directed=True)
        self.g2.add_edge(2, 1, 1, directed=True)
        self.g2.add_edge(3, 4, 1, directed=True)
        self.g2.add_edge(3, 5, 1, directed=True)
        self.g2.add_edge(3, 2, -6, directed=True)
        self.g2.add_edge(4, 5, 1, directed=True)
        self.g2.add_edge(4, 3, 1, directed=True)
        self.g2.add_edge(5, 3, 1, directed=True)
    
    def test_1(self):
        bf = BellmanFordAlgorithm(self.g1)
        inf = math.inf
        self.assertDictEqual({0: 0, 1: 1, 2: -inf, 4: -inf, 3: -inf, 5: 5, 6: 5, 7: 8}, bf.run(0))
        
    def test_2(self):
        bf = BellmanFordAlgorithm(self.g2)
        inf = math.inf
        self.assertDictEqual({0: 0, 1: -inf, 2: -inf, 3: -inf, 4: -inf, 5: -inf}, bf.run(0))
        
        
if __name__ == "__main__":
    unittest.main()