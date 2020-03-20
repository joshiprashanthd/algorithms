from graph_theory.ds.graph import Graph
from graph_theory.tarjans_algo import TarjanAlgorithm
import unittest

class TestTarjanAlgorithm(unittest.TestCase):
    def setUp(self):
        self.g1: Graph = Graph[str]()
        self.g1.add_edge('A', 'B', directed=True)
        self.g1.add_edge('B', 'A', directed=True)
        self.g1.add_edge('A', 'C', directed=True)
        self.g1.add_edge('B', 'D', directed=True)
        self.g1.add_edge('C', 'D', directed=True)
        self.g1.add_edge('D', 'E', directed=True)
        self.g1.add_edge('D', 'F', directed=True)
        self.g1.add_edge('E', 'C', directed=True)
        self.g1.add_edge('E', 'F', directed=True)
        self.g1.add_edge('E', 'G', directed=True)
        self.g1.add_edge('G', 'F', directed=True)
        self.g1.add_edge('F', 'H', directed=True)
        self.g1.add_edge('H', 'G', directed=True)

    def test_1(self):
        ta = TarjanAlgorithm(self.g1)
        self.assertEqual({'A': 1, 'B': 1, 'C': 3, 'D': 3, 'E': 3, 'F': 6, 'G': 6, 'H': 6}, ta.run())


if __name__ == '__main__':
    unittest.main()
