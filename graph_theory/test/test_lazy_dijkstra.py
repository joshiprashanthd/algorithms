import unittest
import __init__

from ds.graph import Graph
from lazy_dijkstra_algo import LazyDijkstra

class TestLazyDijkstra(unittest.TestCase):
    
    def setUp(self):
        self.g1 = Graph[int]()
        self.g1.add_edge(0, 1, 4, directed=True)
        self.g1.add_edge(0, 2, 1, directed=True)
        self.g1.add_edge(2, 1, 2, directed=True)
        self.g1.add_edge(1, 3, 1, directed=True)
        self.g1.add_edge(2, 3, 5, directed=True)
        self.g1.add_edge(3, 4, 3, directed=True)
        
    def test_1(self):
        ld = LazyDijkstra(self.g1)
        min_weights, path = ld.run(0, 4)
        self.assertEqual({0: 0, 1: 3, 2: 1, 3: 4, 4: 7}, min_weights)
        self.assertEqual([0, 2, 1, 3, 4], path)
        
    def test_2(self):
        self.g1.add_edge(3, 5, 7, directed=True)
        self.g1.add_edge(3, 4, 4, directed=True)
        self.g1.add_edge(4, 5, 1, directed=True)
        ld = LazyDijkstra(self.g1)
        _, path = ld.run(2, 5)
        self.assertEqual([2, 1, 3, 4, 5], path)
        
if __name__ == "__main__":
    unittest.main()