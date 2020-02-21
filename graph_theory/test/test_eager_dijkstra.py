import unittest
import __init__

from ds.graph import Graph
from eager_dijkstra_algo import EagerDijkstra

class TestEagerDijkstra(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph[int]()
        self.g1.add_edge(0, 1, 5, directed=True)
        self.g1.add_edge(0, 2, 1, directed=True)
        self.g1.add_edge(1, 2, 2, directed=True)
        self.g1.add_edge(1, 3, 3, directed=True)
        self.g1.add_edge(1, 4, 20, directed=True)
        self.g1.add_edge(2, 1, 3, directed=True)
        self.g1.add_edge(2, 4, 12, directed=True)
        self.g1.add_edge(3, 2, 3, directed=True)
        self.g1.add_edge(3, 4, 2, directed=True)
        self.g1.add_edge(3, 5, 6, directed=True)
        self.g1.add_edge(4, 5, 1, directed=True)
        
    def test_1(self):
        ed = EagerDijkstra(self.g1)
        dist, path = ed.run(0, 5)
        self.assertEqual({0: 0, 1: 4, 2: 1, 3: 7, 4: 9, 5: 10}, dist)
        self.assertEqual([0, 2, 1, 3, 4, 5], path)
        
if __name__ == "__main__":
    unittest.main()