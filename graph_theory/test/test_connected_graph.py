import unittest
import __init__

from ds.graph import Graph
from connected_graphs import ConnectedGraph

class TestConnectedGraph(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph[int]()
        self.g1.add_edge(0, 1)
        self.g1.add_edge(1, 2)
        self.g1.add_edge(2, 0)
        self.g1.add_edge(3, 4)
        self.g1.add_edge(4, 5)
        self.g1.add_edge(6, 7)
        
        self.g2 = Graph[int]()
        self.g2.add_edge(1, 3)
        self.g2.add_edge(4, 5)
        self.g2.add_edge(6, 7)
        self.g2.add_edge(8, 9)
        self.g2.add_edge(10, 11)
        
    def test_1(self):
        cg = ConnectedGraph(self.g1)
        count, components = cg.run()
        self.assertEqual(3, count)
        self.assertDictEqual({0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3}, components)
        
    def test_2(self):
        cg = ConnectedGraph(self.g2)
        count, components = cg.run()
        self.assertEqual(5, count)
        self.assertDictEqual({1: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4, 9: 4, 10: 5, 11: 5}, components)
        
if __name__ == "__main__":
    unittest.main()