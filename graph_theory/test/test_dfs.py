import unittest

from graph_theory.ds.graph import Graph
from graph_theory.dfs import DFS

class TestDFS(unittest.TestCase):
    
    def setUp(self):
        self.g = Graph[int]()
        self.g.add_edge(5, 2)
        self.g.add_edge(2, 6)
        self.g.add_edge(2, 1)
        self.g.add_edge(2, 9)
        self.g.add_edge(6, 1)
        self.g.add_edge(4, 8)
        self.g.add_edge(1, 8)
    
    def test_1(self):
        dfs = DFS(self.g)
        self.assertEqual([5, 2, 6, 1, 8, 4, 9], dfs.run())
        
if __name__ == "__main__":
    unittest.main()