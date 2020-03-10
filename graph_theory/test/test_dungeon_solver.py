import unittest

from graph_theory.ds.grid import Grid
from graph_theory.dungeon_problem import DungeonSolver

class TestDungeonSolver(unittest.TestCase):
    def setUp(self):
        self.grid = Grid[str](5, 5, '.')
        
        obst = '#'
        end = 'E'
        
        self.grid.grid[1][0] = obst
        self.grid.grid[1][1] = obst
        self.grid.grid[1][3] = obst
        self.grid.grid[3][1] = obst
        self.grid.grid[3][2] = obst
        self.grid.grid[4][3] = obst
        self.grid.grid[4][2] = end
        
    def test_1(self):
        ds = DungeonSolver(self.grid)
        self.assertEqual(10, ds.run((0, 0)))

if __name__ == "__main__":
    unittest.main()