import unittest
from graph_theory.ds.graph import Graph, Edge
from graph_theory.prims_algorithms import LazyPrimsAlgorithm


class TestLazyPrimsAlgorithm(unittest.TestCase):

    def setUp(self) -> None:
        self.g1: Graph = Graph[int](directed=False)
        self.g1.add_edge(0, 1, 10)
        self.g1.add_edge(0, 2, 1)
        self.g1.add_edge(0, 3, 4)
        self.g1.add_edge(1, 2, 3)
        self.g1.add_edge(1, 4, 0)
        self.g1.add_edge(2, 5, 8)
        self.g1.add_edge(2, 3, 2)
        self.g1.add_edge(3, 5, 2)
        self.g1.add_edge(3, 6, 7)
        self.g1.add_edge(4, 5, 1)
        self.g1.add_edge(4, 7, 8)
        self.g1.add_edge(5, 6, 6)
        self.g1.add_edge(5, 7, 9)
        self.g1.add_edge(6, 7, 12)

    def test_1(self):
        lpa = LazyPrimsAlgorithm(self.g1)
        cost, edges = lpa.run(0)
        print("cost : ", cost)
        self.assertEqual([
            Edge[int](0, 2, 1),
            Edge[int](2, 3, 2),
            Edge[int](3, 5, 2),
            Edge[int](5, 4, 1),
            Edge[int](4, 1, 0),
            Edge[int](5, 6, 6),
            Edge[int](4, 7, 8),
        ], edges)


if __name__ == '__main__':
    unittest.main()
