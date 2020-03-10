import unittest

from graph_theory.ds.graph import Graph
from graph_theory.topoogical_sort import TopologicalSort

class TestTopologicalSort(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph[int]()
        self.g1.add_edge(1, 2, directed=True)
        self.g1.add_edge(1, 3, directed=True)
        self.g1.add_edge(2, 5, directed=True)
        self.g1.add_edge(2, 6, directed=True)
        self.g1.add_edge(3, 5, directed=True)
        self.g1.add_edge(7, 1, directed=True)
        self.g1.add_edge(7, 8, directed=True)
        
        self.g2 = Graph[str]()
        self.g2.add_edge('A', 'B', directed=True)
        self.g2.add_edge('A', 'C', directed=True)
        self.g2.add_edge('A', 'F', directed=True)
        self.g2.add_edge('B', 'G', directed=True)
        self.g2.add_edge('C', 'D', directed=True)
        self.g2.add_edge('C', 'E', directed=True)
        self.g2.add_edge('C', 'F', directed=True)
        self.g2.add_edge('D', 'E', directed=True)
        self.g2.add_edge('E', 'F', directed=True)
        self.g2.add_edge('E', 'G', directed=True)
        self.g2.add_edge('E', 'H', directed=True)
        
    def test_1(self):
        ts = TopologicalSort(self.g1)
        self.assertEqual([7, 8, 1, 3, 2, 6, 5], ts.run())
        
    def test_2(self):
        ts = TopologicalSort(self.g2)
        self.assertEqual(['A', 'C', 'D', 'E', 'H', 'F', 'B', 'G'], ts.run())
        

if __name__ == "__main__":
    unittest.main()