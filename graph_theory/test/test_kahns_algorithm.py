import unittest

from graph_theory.ds.graph import Graph
from graph_theory.kahns_algorithm import KahnsAlgorithm


class TestKahnsAlgorithm(unittest.TestCase):
    def setUp(self) -> None:
        self.g1 = Graph[int](directed=True)
        self.g1.add_edge(1, 2)
        self.g1.add_edge(1, 3)
        self.g1.add_edge(2, 5)
        self.g1.add_edge(2, 6)
        self.g1.add_edge(3, 5)
        self.g1.add_edge(7, 1)
        self.g1.add_edge(7, 8)

        self.g2 = Graph[int]()
        self.g2.add_edge(1, 2)
        self.g2.add_edge(1, 3)
        self.g2.add_edge(1, 6)
        self.g2.add_edge(2, 7)
        self.g2.add_edge(3, 4)
        self.g2.add_edge(3, 5)
        self.g2.add_edge(3, 6)
        self.g2.add_edge(4, 5)
        self.g2.add_edge(5, 6)
        self.g2.add_edge(5, 7)
        self.g2.add_edge(5, 8)

    def test_1(self):
        ka = KahnsAlgorithm(self.g1)
        self.assertListEqual([7, 8, 1, 2, 3, 5, 6], ka.run())

    def test_2(self):
        ka = KahnsAlgorithm(self.g2)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], ka.run())
