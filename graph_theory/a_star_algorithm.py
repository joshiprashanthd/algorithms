from typing import Union, AnyStr, List, Tuple, Any

from graph_theory.ds.grid import Grid
from graph_theory.ds.point import Point
from graph_theory.ds.priority_queue import PriorityQueue


class AStarAlgorithm:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.rows = self.grid.rows
        self.cols = self.grid.cols
        self.obstacle = 1
        self.free = 0
        self.close = -1

        self.found = False  # found is set to true if the point reaches the end point
        self.resign = False

        self.f = 0
        self.g = 0
        self.cost = 1  # cost for taking each step

        self.heuristic = Grid[int](self.rows, self.cols, 0)  # cost map of each cell
        self.action = Grid[int](self.rows, self.cols, 0)
        self.closed = Grid[int](self.rows, self.cols, 0)  # to prevent path going backwards

        self.start = Point(0, 0)
        self.end = Point(self.rows - 1, self.cols - 1)

        self.up = Point(-1, 0)
        self.left = Point(0, -1)
        self.down = Point(1, 0)
        self.right = Point(0, 1)
        self.deltas = [self.up, self.left, self.down, self.right]

        self.cells = PriorityQueue(maxsize=1000, max_queue=False, sort_index=0)

    def __init_heuristics(self):
        for i in range(self.rows):
            for j in range(self.cols):
                current_point = Point(i, j)
                self.heuristic[i][j] = current_point.absolute_distance_from(self.end)
                if self.grid[i][j] == self.obstacle:
                    self.heuristic[i][j] = 99

    def __reconstruct_path(self):
        invpath = []
        point = self.end
        invpath.append(point)

        while point != self.start:
            point = point - self.deltas[self.action[point.x][point.y]]
            invpath.append(point)

        path = list(reversed(invpath))
        return path

    def run(self) -> Union[AnyStr, List[Tuple[Any, Any]]]:
        self.__init_heuristics()

        self.f = self.g + self.heuristic[self.start.x][self.start.y]
        self.cells.insert((self.f, self.g, self.start))

        while not self.found and not self.resign:
            if self.cells.is_empty():
                return "PATH NOT FOUND"

            self.f, self.g, next_point = self.cells.pop()

            if next_point == self.end:
                self.found = True
            else:
                for index, delta in enumerate(self.deltas):
                    new_point = next_point + delta
                    x = new_point.x
                    y = new_point.y
                    if self.start <= new_point <= self.end:
                        if self.closed[x][y] == self.free and self.grid[x][y] == self.free:
                            g2 = self.g + self.cost
                            f2 = g2 + self.heuristic[x][y]
                            self.cells.insert((f2, g2, new_point))
                            self.closed[x][y] = self.close
                            self.action[x][y] = index

        return self.__reconstruct_path()
