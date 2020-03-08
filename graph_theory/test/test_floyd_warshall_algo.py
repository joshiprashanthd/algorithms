import unittest
import __init__

from floyd_warshall_algo import FloydWarshallAlgorithm
from ds.graph import Graph

class TestFloydWarshallAlgorithm(unittest.TestCase):
    
    def setUp(self):
        self.g = Graph[int]()
        self.g.add_edge(0, 1, 2, directed=True)
        self.g.add_edge(1, 2, 3, directed=True)
        self.g.add_edge(1, 3, 1, directed=True)
        self.g.add_edge(2, 3, 6, directed=True)
        self.g.add_edge(2, 0, 1, directed=True)
        self.g.add_edge(3, 2, 3, directed=True)
        self.g.add_edge(3, 0, 5, directed=True)
        
        self.g1 = Graph[int]()
        self.g1.add_edge(0, 1, 2, directed=True)
        self.g1.add_edge(0, 2, 5, directed=True)
        self.g1.add_edge(0, 6, 10, directed=True)
        self.g1.add_edge(1, 2, 2, directed=True)
        self.g1.add_edge(1, 4, 11, directed=True)
        self.g1.add_edge(2, 6, 2, directed=True)
        self.g1.add_edge(6, 5, 11, directed=True)
        self.g1.add_edge(4, 5, 1, directed=True)
        self.g1.add_edge(5, 4, -2, directed=True)
        
    def test_1(self):
        fw  = FloydWarshallAlgorithm(self.g)
        self.assertEqual(([0, 1, 3], 3), fw.run(0, 3))
        self.assertEqual(([3, 2, 0], 4), fw.run(3, 0))
        
    def test_2(self):
        fw = FloydWarshallAlgorithm(self.g1)
        self.assertEqual(([0, 1, 2, 6], 6), fw.run(0, 6))
        fw.run(1, 6)
        

if __name__ == "__main__":
    unittest.main()        