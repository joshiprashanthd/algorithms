import unittest

from graph_theory.ds.graph import Graph
from graph_theory.detect_cycle import DetectCycle


class TestDetectCycle(unittest.TestCase):
    def setUp(self) -> None:
        self.g1: Graph = Graph[int](directed=True)
        self.g1.add_edge(0, 1)
        self.g1.add_edge(0, 2)
        self.g1.add_edge(1, 2)
        self.g1.add_edge(2, 0)
        self.g1.add_edge(2, 3)
        self.g1.add_edge(3, 3)

        self.g2: Graph = Graph[int](directed=True)
        self.g2.add_edge(1, 2)
        self.g2.add_edge(1, 3)
        self.g2.add_edge(2, 4)
        self.g2.add_edge(2, 5)

    def test_1(self):
        dc = DetectCycle(self.g1)
        self.assertEqual(True, dc.run())

    def test_2(self):
        dc = DetectCycle(self.g2)
        self.assertEqual(False, dc.run())


if __name__ == '__main__':
    unittest.main()