import unittest
from graph_theory.ds.graph import Graph, Edge
from graph_theory.bridges_finding_algo import BridgesFindingAlgorithm


class TestBridgesFindingAlgorithm(unittest.TestCase):
    def setUp(self):
        self.g1: Graph = Graph[str]()
        self.g1.add_edge('A', 'B')
        self.g1.add_edge('A', 'C')
        self.g1.add_edge('B', 'C')
        self.g1.add_edge('C', 'D')
        self.g1.add_edge('D', 'E')
        self.g1.add_edge('C', 'F')
        self.g1.add_edge('F', 'G')
        self.g1.add_edge('G', 'H')
        self.g1.add_edge('H', 'I')
        self.g1.add_edge('I', 'F')

        self.g2: Graph = Graph[str]()
        self.g2.add_edge('A', 'B')
        self.g2.add_edge('B', 'F')
        self.g2.add_edge('B', 'C')
        self.g2.add_edge('C', 'E')
        self.g2.add_edge('C', 'D')
        self.g2.add_edge('E', 'D')
        self.g2.add_edge('F', 'H')
        self.g2.add_edge('F', 'G')
        self.g2.add_edge('H', 'G')
        self.g2.add_edge('G', 'I')
        self.g2.add_edge('I', 'J')
        self.g2.add_edge('J', 'K')
        self.g2.add_edge('J', 'L')
        self.g2.add_edge('K', 'L')

    def test_1(self):
        bf = BridgesFindingAlgorithm(self.g1)
        self.assertEqual(['D', 'E', 'C', 'D', 'C', 'F'], bf.run())

    def test_2(self):
        bf = BridgesFindingAlgorithm(self.g2)
        self.assertEqual(['I', 'J', 'G', 'I', 'B', 'F', 'B', 'C', 'A', 'B'], bf.run())


if __name__ == '__main__':
    unittest.main()
