import unittest

from graph_theory.ds.graph import Graph
from graph_theory.topoogical_sort import TopologicalSort

class TestTopologicalSort(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph[int]()
        self.g1.add_edge(1, 2)
        self.g1.add_edge(1, 3)
        self.g1.add_edge(2, 5)
        self.g1.add_edge(2, 6)
        self.g1.add_edge(3, 5)
        self.g1.add_edge(7, 1)
        self.g1.add_edge(7, 8)
        
        self.g2 = Graph[str]()
        self.g2.add_edge('A', 'B')
        self.g2.add_edge('A', 'C')
        self.g2.add_edge('A', 'F')
        self.g2.add_edge('B', 'G')
        self.g2.add_edge('C', 'D')
        self.g2.add_edge('C', 'E')
        self.g2.add_edge('C', 'F')
        self.g2.add_edge('D', 'E')
        self.g2.add_edge('E', 'F')
        self.g2.add_edge('E', 'G')
        self.g2.add_edge('E', 'H')
        
    def test_1(self):
        ts = TopologicalSort(self.g1)
        self.assertEqual([7, 8, 1, 3, 2, 6, 5], ts.run())
        
    def test_2(self):
        ts = TopologicalSort(self.g2)
        self.assertEqual(['A', 'C', 'D', 'E', 'H', 'F', 'B', 'G'], ts.run())
        

if __name__ == "__main__":
    unittest.main()