import unittest
import __init__

from ds.graph import Graph
from bfs import BFS

class TestBFS(unittest.TestCase):
    
    def setUp(self):
        self.g1 = Graph[int]()
        self.g1.add_edge(1, 2)
        self.g1.add_edge(1, 6)
        self.g1.add_edge(2, 4)
        self.g1.add_edge(3, 5)
        self.g1.add_edge(3, 6)
        self.g1.add_edge(4, 9)
        self.g1.add_edge(4, 6)
        self.g1.add_edge(4, 8)
        self.g1.add_edge(9, 8)
        self.g1.add_edge(5, 8)
        
        self.g2 = Graph[str]()
        self.g2.add_edge('A', 'B')
        self.g2.add_edge('A', 'C')
        self.g2.add_edge('A', 'F')
        self.g2.add_edge('B', 'G')
        self.g2.add_edge('C', 'D')
        self.g2.add_edge('C', 'E')
        self.g2.add_edge('C', 'F')
        self.g2.add_edge('D', 'E')
        self.g2.add_edge('E', 'F')
        self.g2.add_edge('E', 'G')
        self.g2.add_edge('E', 'H')
    
    def test_1(self):
        bfs = BFS(self.g1)
        self.assertEqual([1, 2, 4, 8], bfs.run(1, 8))
        
    def test_2(self):
        bfs = BFS(self.g2)
        self.assertEqual(['A', 'C', 'E'], bfs.run('A', 'E'))
        
        
        
    def test_3(self):
        bfs = BFS(self.g2)
        self.assertEqual(['F', 'E', 'H'], bfs.run('F', 'H'))
        
    def test_4(self):
        bfs = BFS(self.g2)
        self.g2.remove_edge('A', 'C')
        self.assertEqual(['A', 'F', 'E'], bfs.run('A', 'E'))
        self.g2.add_edge('A', 'C')
        
    def test_5(self):
        bfs = BFS(self.g2)
        self.g2.remove_edge('A', 'C')
        self.g2.remove_edge('F', 'E')
        self.g2.remove_edge('F', 'C')
        self.assertEqual(['A', 'B', 'G', 'E', 'D'], bfs.run('A', 'D'))

if __name__ == "__main__":
    unittest.main()
        