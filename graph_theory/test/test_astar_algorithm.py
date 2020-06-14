import unittest

from graph_theory.a_star_algorithm import AStarAlgorithm
from graph_theory.ds.grid import Grid
from graph_theory.ds.point import Point


class TestAStarAlgorithm(unittest.TestCase):

    def setUp(self) -> None:
        self.grid1 = Grid[int](5, 6, char=0)
        self.grid1.grid[0][1] = 1
        self.grid1.grid[1][1] = 1
        self.grid1.grid[0][2] = 1
        self.grid1.grid[0][5] = 1
        self.grid1.grid[1][5] = 1
        self.grid1.grid[2][5] = 1
        self.grid1.grid[2][3] = 1
        self.grid1.grid[3][3] = 1
        self.grid1.grid[3][1] = 1
        self.grid1.grid[4][3] = 1
        self.grid1.grid[4][4] = 1

        self.grid2 = Grid[int](10, 10, 0)

        for x, y in zip([8, 6, 7, 7, 5, 4, 4, 4, 1, 1, 1, 3, 7, 8, 9, 5], [9, 7, 5, 4, 4, 5, 6, 7, 0, 1, 2, 3, 3, 3, 3, 8]):
            self.grid2.grid[x][y] = 1

    def test_1(self):
        astar = AStarAlgorithm(self.grid1)
        self.assertListEqual([Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1), Point(2, 2), Point(1, 2),
                              Point(1, 3), Point(1, 4), Point(2, 4), Point(3, 4), Point(3, 5), Point(4, 5)], astar.run())

    def test_2(self):
        astar = AStarAlgorithm(self.grid2)
        self.assertListEqual([Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3), Point(1, 3), Point(2, 3), Point(2, 4), Point(3, 4),
                              Point(3, 5), Point(3, 6), Point(3, 7), Point(3, 8), Point(4, 8), Point(4, 9), Point(5, 9), Point(6, 9),
                              Point(7, 9), Point(7, 8), Point(8, 8), Point(9, 8), Point(9, 9)], astar.run())


if __name__ == '__main__':
    unittest.main()