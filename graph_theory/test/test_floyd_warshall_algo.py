import unittest
import __init__

from graph_theory.floyd_warshall_algo import FloydWarshallAlgorithm
from graph_theory.ds.graph import Graph


class TestFloydWarshallAlgorithm(unittest.TestCase):

    def setUp(self):
        self.g = Graph[int]()
        self.g.add_edge(0, 1, 2)
        self.g.add_edge(1, 2, 3)
        self.g.add_edge(1, 3, 1)
        self.g.add_edge(2, 3, 6)
        self.g.add_edge(2, 0, 1)
        self.g.add_edge(3, 2, 3)
        self.g.add_edge(3, 0, 5)

        self.g1 = Graph[int]()
        self.g1.add_edge(0, 1, 2)
        self.g1.add_edge(0, 2, 5)
        self.g1.add_edge(0, 6, 10)
        self.g1.add_edge(1, 2, 2)
        self.g1.add_edge(1, 4, 11)
        self.g1.add_edge(2, 6, 2)
        self.g1.add_edge(6, 5, 11)
        self.g1.add_edge(4, 5, 1)
        self.g1.add_edge(5, 4, -2)

    def test_1(self):
        fw = FloydWarshallAlgorithm(self.g)
        self.assertEqual(([0, 1, 3], 3), fw.run(0, 3))
        self.assertEqual(([3, 2, 0], 4), fw.run(3, 0))

    def test_2(self):
        fw = FloydWarshallAlgorithm(self.g1)
        self.assertEqual(([0, 1, 2, 6], 6), fw.run(0, 6))


if __name__ == "__main__":
    unittest.main()
