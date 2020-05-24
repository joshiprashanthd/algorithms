import unittest

from graph_theory.ds.graph import Graph
from graph_theory.eulerian_path import EulerianPathFinder


class TestEulerianPathFinder(unittest.TestCase):

    def setUp(self) -> None:
        self.g1: Graph = Graph[int](directed=True)
        self.g1.add_edge(1, 2)
        self.g1.add_edge(1, 3)
        self.g1.add_edge(2, 2)
        self.g1.add_edge(2, 4)
        self.g1.add_edge(2, 4)
        self.g1.add_edge(3, 1)
        self.g1.add_edge(3, 2)
        self.g1.add_edge(3, 5)
        self.g1.add_edge(4, 3)
        self.g1.add_edge(4, 6)
        self.g1.add_edge(5, 6)
        self.g1.add_edge(6, 3)

    def test1(self):
        epf = EulerianPathFinder(self.g1)
        self.assertListEqual([1, 3, 5, 6, 3, 2, 4, 3, 1, 2, 2, 4, 6], epf.run())

    if __name__ == '__main__':
        unittest.main()
