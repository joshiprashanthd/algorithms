from graph_theory.ds.graph import Graph
from graph_theory.tarjans_algo import TarjanAlgorithm
import unittest

class TestTarjanAlgorithm(unittest.TestCase):
    def setUp(self):
        self.g1: Graph = Graph[str]()
        self.g1.add_edge('A', 'B')
        self.g1.add_edge('B', 'A')
        self.g1.add_edge('A', 'C')
        self.g1.add_edge('B', 'D')
        self.g1.add_edge('C', 'D')
        self.g1.add_edge('D', 'E')
        self.g1.add_edge('D', 'F')
        self.g1.add_edge('E', 'C')
        self.g1.add_edge('E', 'F')
        self.g1.add_edge('E', 'G')
        self.g1.add_edge('G', 'F')
        self.g1.add_edge('F', 'H')
        self.g1.add_edge('H', 'G')

    def test_1(self):
        ta = TarjanAlgorithm(self.g1)
        self.assertEqual({'A': 1, 'B': 1, 'C': 3, 'D': 3, 'E': 3, 'F': 6, 'G': 6, 'H': 6}, ta.run())


if __name__ == '__main__':
    unittest.main()
