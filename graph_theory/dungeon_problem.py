# You are trapped in a 2D dungeon and need to find the 
# quickest way out! The dungeon is composed of unit cubes which
# may or may not be filled with rock. It takes one minute to
# move one unit north, south, east and west. You cannot move diagonally
# and the maze is surrounded by solid rock on all sides.

# Is an escape possible? If yes, how long will it take?

from typing import List, Dict, Tuple
from ds.grid import Grid

class DungeonSolver:
    def __init__(self, grid: Grid):
        
        # Grid object
        self.grid = grid
        
        # Queues of row value and columns value of a cell
        self.qr: List[int] = []
        self.qc: List[int] = []
        
        # Matrix to track the whether the cell is visited or not
        self.visited: Grid = Grid[bool](self.grid.rows, self.grid.cols, False)
        
        # Number of nodes being added in Breadth First Search Expansion
        self.nodes_in_next_layer = 0
        
        # Direction vectors, used to move Left, Right, Up and Down
        self.dr = [-1, 1, 0, 0]
        self.dc = [0, 0, 1, -1]
        
    def run(self, start: Tuple[int, int]) -> None:
        self.qr.append(start[0])
        self.qc.append(start[1])
        self.visited.grid[start[0]][start[1]] = True
        
        # Track whether we encountered symbol E in the grid
        reached_end = False
        
        # Used to track number of steps taken
        move_count = 0
        
        # Tracks number of nodes in the queue to dequeue
        nodes_left_in_layer = 1

        while len(self.qr) > 0:
            curr_row = self.qr.pop(0)
            curr_col = self.qc.pop(0)
            
            if self.grid.grid[curr_row][curr_col] == 'E':
                reached_end = True
                break
            
            self.__explore_neighbors(curr_row, curr_col)
                
            nodes_left_in_layer -= 1
            
            if nodes_left_in_layer == 0:
                nodes_left_in_layer = self.nodes_in_next_layer
                self.nodes_in_next_layer = 0
                move_count += 1
        if reached_end:
            return move_count
        return -1

        
    def __explore_neighbors(self, row: int, col: int):
        for i in range(4):
            rr = row + self.dr[i]
            cc = col + self.dc[i]
            
            # Conditions to track whether we reached the boundary of grid
            if rr < 0 or cc < 0: continue
            if rr >= self.grid.rows or cc >= self.grid.cols: continue
            
            # Skip visited locations or blocked cells
            if self.visited.grid[rr][cc]: continue
            if self.grid.grid[rr][cc] == '#': continue
                
            self.qr.append(rr)
            self.qc.append(cc)
            
            self.visited.grid[rr][cc] = True
            self.nodes_in_next_layer += 1