from typing import List, Generic, TypeVar

T = TypeVar('T')

class Grid(Generic[T]):
    def __init__(self, rows: int, cols: int, char: T) -> None:
        self.rows = rows
        self.cols = cols
        self.char = char
        self.grid: List[List[T]]
        self.__init_grid()
        
    def __init_grid(self):
        self.grid = []
        
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.cols):
                self.grid[i].append(self.char)
    
    def get(self, row: int, col: int) -> T:
        return self.grid[row][col]
    
    def __str__(self):
        return '\n'.join([' '.join([col for col in row]) for row in self.grid])
    